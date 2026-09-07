import copy
from datetime import date
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from test_engine_quality import load_script

GATE = load_script('check_source_freshness.py')


class SourceFreshnessNegativeTests(unittest.TestCase):
    def payload(self):
        return {'records': [dict(id=domain, domain=domain, jurisdiction='test',
            title='Synthetic fixture', publisher='Test publisher', tier=1,
            url='https://example.com/source', verified_on='2026-01-01',
            review_every_days=30, next_review='2026-01-31',
            use_for=['fixture testing'], verification_note='Synthetic; not verified source evidence')
            for domain in sorted(GATE.DOMAINS)]}

    def check(self, payload, as_of=date(2026, 1, 1)):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'register.json'
            path.write_text(json.dumps(payload), encoding='utf-8')
            return GATE.validate(path, as_of)

    def test_valid_window_and_future_verification(self):
        self.assertEqual([], self.check(self.payload()))
        self.assertTrue(any('future' in e for e in self.check(self.payload(), date(2025, 12, 31))))

    def test_malformed_fields_reject_without_crashing(self):
        for field, value in (('id', []), ('domain', {}), ('url', {}),
                             ('url', 'https://['), ('tier', True), ('use_for', [None]),
                             ('review_every_days', True), ('review_every_days', 1.5),
                             ('review_every_days', 10**20)):
            with self.subTest(field=field, value=value):
                payload = copy.deepcopy(self.payload())
                payload['records'][0][field] = value
                self.assertTrue(self.check(payload))

    def test_nonobject_root_and_duplicate_id_reject(self):
        for payload in ([], None, 'text', {'records': []}):
            self.assertTrue(self.check(payload))
        payload = self.payload()
        payload['records'].append(copy.deepcopy(payload['records'][0]))
        self.assertTrue(any('duplicate' in e for e in self.check(payload)))

    def test_url_authority_validation_and_cli_exit(self):
        # Synthetic locators only; the checker must not make network requests.
        cases = (
            ('https://example.com:bad/source', False),
            ('https://example.com:99999/source', False),
            ('https://example.com:-1/source', False),
            ('https://@example.com/source', False),
            ('https://:@example.com/source', False),
            ('https://user:password@example.com/source', False),
            ('https://example.com/source', True),
            ('https://example.com:443/source', True),
            ('https://example.com:8443/source', True),
        )
        with tempfile.TemporaryDirectory() as temp:
            register = Path(temp) / 'register.json'
            for url, accepted in cases:
                with self.subTest(url=url):
                    payload = self.payload()
                    payload['records'][0]['url'] = url
                    register.write_text(json.dumps(payload), encoding='utf-8')
                    errors = GATE.validate(register, date(2026, 1, 1))
                    if accepted:
                        self.assertEqual([], errors)
                    else:
                        self.assertTrue(any('url must be' in error for error in errors))
                    result = subprocess.run(
                        [sys.executable, '-X', 'utf8', GATE.__file__,
                         '--register', str(register), '--as-of', '2026-01-01'],
                        capture_output=True, text=True, timeout=10,
                    )
                    self.assertEqual(0 if accepted else 1, result.returncode,
                                     result.stdout + result.stderr)
                    self.assertEqual('', result.stderr)
                    self.assertIn('source freshness: PASS' if accepted else
                                  'source freshness: FAIL', result.stdout)
                    if accepted:
                        self.assertIn('claim support NOT ASSESSED', result.stdout)
