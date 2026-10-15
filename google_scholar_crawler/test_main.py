import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from main import main, write_stats


class CitationDataTests(unittest.TestCase):
    def test_total_uses_scholar_count_and_preserves_paper_ids(self):
        author = {
            'name': 'Test Author 测试',
            'citedby': 42,
            'publications': [
                {'author_pub_id': 'author:paper', 'num_citations': 5},
                {'author_pub_id': 'author:uncited', 'num_citations': 0},
            ],
        }
        with tempfile.TemporaryDirectory() as directory:
            write_stats(author, directory)
            data = json.loads((Path(directory) / 'gs_data.json').read_text())
            badge = json.loads((Path(directory) / 'gs_data_shieldsio.json').read_text())
        self.assertEqual(data['citedby'], 42)
        self.assertEqual(data['publications']['author:uncited']['num_citations'], 0)
        self.assertEqual(data['name'], author['name'])
        self.assertTrue(data['updated'].endswith('+00:00'))
        self.assertEqual(badge, {'schemaVersion': 1, 'label': 'citations', 'message': '42'})
        self.assertIsInstance(author['publications'], list)

    def test_zero_citations_are_valid(self):
        with tempfile.TemporaryDirectory() as directory:
            write_stats({'citedby': 0, 'publications': []}, directory)
            badge = json.loads((Path(directory) / 'gs_data_shieldsio.json').read_text())
        self.assertEqual(badge['message'], '0')

    def test_invalid_response_preserves_previous_data(self):
        invalid_authors = [
            {'publications': []},
            {'citedby': -1, 'publications': []},
            {'citedby': '42', 'publications': []},
            {'citedby': True, 'publications': []},
            {'citedby': 42},
            {'citedby': 42, 'publications': [{'num_citations': 1}]},
            {'citedby': 42, 'publications': [{'author_pub_id': 'a:p', 'num_citations': None}]},
        ]
        with tempfile.TemporaryDirectory() as directory:
            files = [Path(directory) / 'gs_data.json', Path(directory) / 'gs_data_shieldsio.json']
            for file in files:
                file.write_text('previous valid data')
            for author in invalid_authors:
                with self.subTest(author=author), self.assertRaises((ValueError, KeyError)):
                    write_stats(author, directory)
                for file in files:
                    self.assertEqual(file.read_text(), 'previous valid data')

    def test_missing_scholar_id_fails_clearly(self):
        with patch.dict(os.environ, {'GOOGLE_SCHOLAR_ID': ' '}):
            with self.assertRaisesRegex(ValueError, 'GOOGLE_SCHOLAR_ID'):
                main()


if __name__ == '__main__':
    unittest.main()
