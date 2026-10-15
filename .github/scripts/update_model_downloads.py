"""Publish cumulative Hugging Face downloads for the homepage's model groups."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


MODEL_GROUPS = {
    'iris': ('AllSpark-Research/Iris-mini', 'AllSpark-Research/Iris-pro'),
    'mirothinker-v1': (
        'miromind-ai/MiroThinker-v1.0-8B',
        'miromind-ai/MiroThinker-v1.0-30B',
        'miromind-ai/MiroThinker-v1.0-72B',
    ),
}


def fetch_model(model_id):
    url = f'https://huggingface.co/api/models/{quote(model_id, safe="/")}?expand[]=downloadsAllTime'
    request = Request(url, headers={'User-Agent': 'circleLZY-homepage-model-downloads/1.0'})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except (URLError, TimeoutError) as error:
            if isinstance(error, HTTPError) and error.code != 429 and error.code < 500:
                raise
            if attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))


def write_stats(models, output_dir):
    # Validate every expected model before writing anything. Missing counts must
    # never silently become zero or a partial total. "downloads" is only 30 days.
    groups = {}
    for group, model_ids in MODEL_GROUPS.items():
        counts = {}
        for model_id in model_ids:
            model = models.get(model_id)
            if not isinstance(model, dict) or model.get('id') != model_id:
                raise ValueError(f'Missing or unexpected model: {model_id}')
            count = model.get('downloadsAllTime')
            if type(count) is not int or count < 0:
                raise ValueError(f'Invalid cumulative download count: {model_id}')
            counts[model_id] = count
        groups[group] = {'total': sum(counts.values()), 'models': counts}

    data = {
        'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'metric': 'downloadsAllTime',
        'groups': groups,
    }
    files = {'downloads.json': data}
    for group, stats in groups.items():
        files[f'{group}.json'] = {
            'schemaVersion': 1,
            'label': 'downloads',
            'message': f'{stats["total"]:,}',
            'color': 'yellow',
            'cacheSeconds': 3600,
        }

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, payload in files.items():
        (output_dir / filename).write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_dir', type=Path)
    args = parser.parse_args()
    models = {model_id: fetch_model(model_id)
              for model_ids in MODEL_GROUPS.values() for model_id in model_ids}
    data = write_stats(models, args.output_dir)
    for group, stats in data['groups'].items():
        print(f'{group}: {stats["total"]:,} cumulative downloads')


if __name__ == '__main__':
    main()
