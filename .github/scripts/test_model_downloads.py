import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from update_model_downloads import MODEL_GROUPS, fetch_model, write_stats


class ModelDownloadTests(unittest.TestCase):
    def setUp(self):
        self.models = {
            model_id: {'id': model_id, 'downloadsAllTime': count, 'downloads': 999}
            for count, model_id in enumerate(
                (model_id for group in MODEL_GROUPS.values() for model_id in group)
            )
        }

    def test_sums_cumulative_counts_including_zero_and_excludes_other_versions(self):
        self.models['miromind-ai/MiroThinker-v1.5-30B'] = {
            'id': 'miromind-ai/MiroThinker-v1.5-30B', 'downloadsAllTime': 100000,
        }
        with tempfile.TemporaryDirectory() as directory:
            data = write_stats(self.models, directory)
            self.assertEqual(data['groups']['iris']['total'], 1)
            self.assertEqual(data['groups']['mirothinker-v1']['total'], 9)
            self.assertEqual(data['metric'], 'downloadsAllTime')
            badge = json.loads((Path(directory) / 'mirothinker-v1.json').read_text())
            self.assertEqual(badge['schemaVersion'], 1)
            self.assertEqual(badge['message'], '9')

    def test_incomplete_or_invalid_response_preserves_all_published_files(self):
        model_id = MODEL_GROUPS['mirothinker-v1'][-1]
        invalid_models = [None, {}, {'id': 'wrong/model', 'downloadsAllTime': 5}]
        invalid_models += [{'id': model_id, 'downloadsAllTime': value}
                           for value in (None, -1, '10', True)]
        invalid_models.append({'id': model_id, 'downloads': 123})
        with tempfile.TemporaryDirectory() as directory:
            write_stats(self.models, directory)
            previous = {file: file.read_bytes() for file in Path(directory).iterdir()}
            for invalid in invalid_models:
                models = copy.deepcopy(self.models)
                models[model_id] = invalid
                with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                    write_stats(models, directory)
                for file, contents in previous.items():
                    self.assertEqual(file.read_bytes(), contents)

    @patch('update_model_downloads.time.sleep')
    @patch('update_model_downloads.urlopen', side_effect=URLError('unavailable'))
    def test_network_retries_are_bounded(self, urlopen, sleep):
        with self.assertRaises(URLError):
            fetch_model(MODEL_GROUPS['iris'][0])
        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    @patch('update_model_downloads.time.sleep')
    @patch('update_model_downloads.urlopen',
           side_effect=HTTPError('https://huggingface.co/', 404, 'Not found', {}, None))
    def test_missing_model_fails_without_retry(self, urlopen, sleep):
        with self.assertRaises(HTTPError):
            fetch_model(MODEL_GROUPS['iris'][0])
        self.assertEqual(urlopen.call_count, 1)
        sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
