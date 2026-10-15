"""Refresh the public Google Scholar data consumed by the homepage."""

import json
from datetime import datetime, timezone
import os
from pathlib import Path
import sys


def write_stats(author, output_dir):
    """Validate a complete response before replacing the published JSON files."""
    citations = author.get('citedby')
    if type(citations) is not int or citations < 0:
        raise ValueError('Google Scholar did not return a valid total citation count')

    publications = {}
    for paper in author['publications']:
        paper_id = paper['author_pub_id']
        count = paper.get('num_citations')
        if type(count) is not int or count < 0:
            raise ValueError('Google Scholar returned an invalid paper citation count')
        publications[paper_id] = paper

    data = dict(author)
    data['updated'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    data['publications'] = publications
    badge = {'schemaVersion': 1, 'label': 'citations', 'message': str(citations)}

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, payload in [('gs_data.json', data), ('gs_data_shieldsio.json', badge)]:
        (output_dir / filename).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
        )
    return data


def main():
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', '').strip()
    if not scholar_id:
        raise ValueError('The GOOGLE_SCHOLAR_ID repository secret is missing or empty')

    # Import here so dependency failures also produce a readable Actions annotation.
    from scholarly import scholarly

    scholarly.set_timeout(30)
    scholarly.set_retries(2)
    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    if author.get('scholar_id') != scholar_id:
        raise ValueError('Google Scholar returned an unexpected author profile')

    data = write_stats(author, 'results')
    print(f"Updated {data['name']}: {data['citedby']} citations, "
          f"{len(data['publications'])} publications at {data['updated']}")


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        message = f'{type(error).__name__}: {error}'
        message = message.replace('%', '%25').replace('\r', '%0D').replace('\n', '%0A')
        print(f'::error title=Google Scholar update failed::{message}', file=sys.stderr)
        raise
