# Independent review: source-freshness checker

Current disposition: RESOLVED by the authorised repair and execution recorded
under [URL repair disposition](#url-repair-disposition). The original negative
evidence below is retained.

Original review verdict: complete the URL validation before accepting the hardening as finished.
The scoped tests pass, but malformed ports still produce successful validation
and CLI completion. This is an inherited false pass left open by the modified
URL block, not a newly introduced regression. Evidence:
[changed URL guard](../../scripts/check_source_freshness.py#L69) and the
[reviewer reproduction](#url-reproduction) below (synthesis).

Scope: current changes to `scripts/check_source_freshness.py`, the new
`tests/test_source_freshness_negative.py`, and the changed freshness test in
`tests/test_engine_quality.py`. Read the repository agent guide, README, local
Kaizen skill/adoption plan, and applicable evidence/anti-slop instructions.
Only this report was written. No source-register or implementation edits,
networking, or other engine work were performed.

## Medium: incomplete URL validation permits malformed source locators

The guard checks scheme, hostname, and truthy username/password values, but
does not access `parsed.port`. In the local reproduction, a non-numeric port
and an out-of-range port passed both `validate()` and `main()`, although reading
the same parsed URL's port raised `ValueError`. This defeats the modified
block's malformed-URL rejection. Evidence:
[guard](../../scripts/check_source_freshness.py#L70) and
[observed results](#url-reproduction) (synthesis).

There is also a smaller presence-check gap in that block: an empty user-info
component is accepted because `parsed.username` is an empty string. If the
intended rule excludes user-info entirely, test `is not None` instead of
truthiness for username/password. This is a demonstrated syntax-policy gap,
not evidence of credential disclosure or exploitation.

Recommended repair: evaluate `parsed.port` inside the existing exception
handler, reject user-info by presence, and add negative cases for malformed
ports and empty user-info alongside a valid explicit-port case. Exercise CLI
failure as well as the returned error list. These are proposed acceptance
checks (inference). The new [malformed-field test](../../tests/test_source_freshness_negative.py#L31)
currently covers malformed brackets and a non-string URL, but not these cases.

No other concrete defect was established in the reviewed changes. The strict
field checks, future-verification rejection, and interval-overflow handling
passed the scoped tests. The revised success message limits its assertion to
review windows and explicitly leaves claim support unassessed. Evidence:
[checker](../../scripts/check_source_freshness.py),
[new tests](../../tests/test_source_freshness_negative.py), and execution below
(synthesis).

## Reviewer execution evidence

Focused commands, run from the repository:

```powershell
python -X utf8 -m unittest discover -s tests -p test_source_freshness_negative.py -v
```

The changed existing test was run separately by adding `tests` to `sys.path`
and loading
`test_engine_quality.EngineQualityTests.test_source_register_window_at_observed_audit_date`
through `unittest.defaultTestLoader`. Observed summaries, reproduced verbatim:

```text
Ran 3 tests in 0.041s

OK
```

```text
Ran 1 test in 0.002s

OK
```

That existing test is a fixed-date, local review-window check. Its pass does
not establish live freshness, URL availability, or claim support.

### URL reproduction

Run the following Python from the repository. It reuses the explicitly
synthetic payload in the new tests and patches reads in memory. The URL
strings are deliberately synthetic malformed variants of that fixture's URL;
they are not cited sources and no network request is made.

```python
import sys, json, io
from pathlib import Path
from datetime import date
from types import SimpleNamespace
from unittest.mock import patch
from contextlib import redirect_stdout
from urllib.parse import urlparse
sys.path.insert(0, 'tests')
from test_source_freshness_negative import GATE, SourceFreshnessNegativeTests

for label, url in [
    ('invalid-port', 'https://example.com:bad/source'),
    ('out-of-range-port', 'https://example.com:99999/source'),
    ('empty-userinfo', 'https://@example.com/source'),
    ('normal', 'https://example.com/source'),
]:
    payload = SourceFreshnessNegativeTests().payload()
    payload['records'][0]['url'] = url
    options = SimpleNamespace(register=Path('in-memory-register.json'),
                              as_of=date(2026, 1, 1))
    with patch.object(Path, 'read_text', return_value=json.dumps(payload)), \
         patch.object(GATE, 'parse_args', return_value=options):
        errors = GATE.validate(options.register, options.as_of)
        with redirect_stdout(io.StringIO()):
            code = GATE.main()
    try:
        port_result = repr(urlparse(url).port)
    except ValueError as exc:
        port_result = type(exc).__name__ + ': ' + str(exc)
    print(label, 'findings=' + repr(errors), 'exit=' + str(code),
          'parsed_port=' + port_result,
          'username=' + repr(urlparse(url).username))
```

Observed output, reproduced verbatim:

```text
invalid-port findings=[] exit=0 parsed_port=ValueError: Port could not be cast to integer value as 'bad' username=None
out-of-range-port findings=[] exit=0 parsed_port=ValueError: Port out of range 0-65535 username=None
empty-userinfo findings=[] exit=0 parsed_port=None username=''
normal findings=[] exit=0 parsed_port=None username=None
```

Supplementary in-memory checks injected `FileNotFoundError` and `UnicodeError`
from `Path.read_text`, and supplied malformed JSON. Each returned a read/JSON
finding without crashing. The synthetic test payload was also accepted on its
review date and rejected as overdue on the following day. These are local
function probes, not additional committed tests or actual permission/encoding
failure fixtures.

## Limits and snapshot

Currentness preflight: `NO_TIME_SENSITIVE_CLAIMS` about external platforms,
markets, law, or source truth. Evidence is context-bound to the inspected code
and local execution. Live source availability, semantic support, production
behaviour, and other host environments remain `NOT_ASSESSED`. No engine score
or general release certification is assigned.

Baseline observed with `git rev-parse HEAD`:
`1ce4f2e7ca5f1f81626d63a63fbea2e4e8631146`.
Reviewed hashes observed with `Get-FileHash`:

```text
scripts/check_source_freshness.py
192BC983FC423E210456D5C1843B92D3751AB0493701BF35253AFF7D55206916
tests/test_source_freshness_negative.py
9804ED96CC7E44BE12F784809DC027C23BD46F36CA2B51BB5C7F2D127D1C9970
tests/test_engine_quality.py
33ADDEF2A5E8B77A522CFE4F561CD9A2D13CF3F305FE276F2C941187065B3ACB
```

Handoff: the implementation owner should close the URL cases and rerun the
focused tests and reproduction. Repair sign-off remains `NOT_ASSESSED`.

## URL repair disposition

The malformed-port and empty-user-info findings are closed for this repaired
snapshot. This supersedes the original pending handoff above. The same agent
implemented the authorised fix and verified it; this is not a separate
independent review of that agent's implementation.

The URL guard now accesses `parsed.port` inside its `ValueError` handler and
rejects username/password components by presence. The new regression test
checks the function result and real subprocess exit/output for malformed ports,
empty or populated user-info, and valid URLs with or without explicit ports.
Evidence: [repaired guard](../../scripts/check_source_freshness.py#L69),
[regression test](../../tests/test_source_freshness_negative.py), and the full
suite result below (synthesis).

Executed from the repository:

```powershell
python -X utf8 -m unittest discover -s tests -p "test_*.py" -v
python -X utf8 scripts/check_source_freshness.py --as-of 2026-09-06
git diff --check -- scripts/check_source_freshness.py tests/test_source_freshness_negative.py
```

Observed suite summary and freshness output, reproduced verbatim:

```text
Ran 20 tests in 0.926s

OK
```

```text
source freshness: PASS (17 records within review windows; as of 2026-09-06; claim support NOT ASSESSED)
```

The whitespace check reported no errors. The freshness result assesses only
record structure and review windows at the requested date; it does not establish
live source availability or semantic claim support.

Source verification dates were not changed. Before and after the repair,
`Get-FileHash docs/source-registers/source-register.json` returned the identical
hash below. Existing unrelated worktree changes were preserved.

```text
docs/source-registers/source-register.json
FFF9B4DB867C59F24A44E3749E0F1FFE267538B1704188738E76ABF362A8DA49
```

Repaired implementation/test hashes observed with `Get-FileHash`:

```text
scripts/check_source_freshness.py
CC6AE062F66737A622ED5836D9262ACD97FD3326BCA0D2DE525F01282D0FACC1
tests/test_source_freshness_negative.py
34E61D3F9E6E73236B46CE7335632BA44DCA7D31635F4CC4AD44C86F078740D2
```
