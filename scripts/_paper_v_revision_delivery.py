#!/usr/bin/env python3
"""Temporary branch-only build delivery. Never writes to main."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import fitz

BASE = '4b6982ac3124bfd24176510fd98829607c82c11c'
BRANCH = 'paper-v/audit-followup-2026-10-05'
SOURCE = 'papers/05-polynomial-flags/polynomial-flag-exponential-periods.tex'
PDF = 'output/pdf/polynomial-flag-exponential-periods.pdf'
MANIFEST = 'output/pdf/manifest.json'
NOTE = 'notes/provenance/paper-v-audit-followup-2026-10-05.md'
REPORT = 'notes/provenance/paper-v-audit-followup-build-2026-10-05.json'
EXPECTED_SOURCE = 'f3a49ad33b6f58f38e6cbb2d211392d6b4f682b5a7dd8ce2e608097d32c2e655'
LOCAL_TEXT = '46cc9987f52b8b10e7bb137c1ba41784c3640e69e9f76f51ceb26af3dd3136da'
LOCAL_RENDER = '9b979b253aedecfd1ff4e3337f6423ff0ca7c84449e59d4b63795d70caff90cf'
assert os.environ['GITHUB_REF_NAME'] == BRANCH
assert fitz.VersionBind == '1.26.7'

def digest(b):
    return hashlib.sha256(b).hexdigest()

def prior(path):
    return subprocess.check_output(['git', 'show', BASE + ':' + path])

def replace(path, old, new):
    p = Path(path)
    s = p.read_text()
    assert s.count(old) == 1, (path, old[:80])
    p.write_text(s.replace(old, new))

assert Path(SOURCE).exists() and digest(Path(SOURCE).read_bytes()) == EXPECTED_SOURCE
replace('README.md',
    "Paper V's actual elliptic independence proofs do not use Paper IV or the companion formal comparison theorems; Papers II–III enter its formal-period interpretations.",
    "Paper V also gives a localized fixed-chain Stokes presentation over actual boundary coefficients. After specializing the nonzero algebraic parameter, Paper III identifies the fixed-face formal coefficient algebra; the resulting localized numerical formal comparison is stated as a proposition. This does not assert a generic formal boundary theorem or an unlocalized cancellation theorem. The actual elliptic independence proofs use neither Paper IV nor the companion formal comparison theorems; Paper II is used only for the separate single-phase formal interpretation.")
replace('notes/repository-status.md',
    '| Paper V | The unsupported earlier general endpoint-complete theorem was withdrawn. The current manuscript proves general polynomial boundary systems and the explicit elliptic fixed-triangle comparison; broader multiblock formal completeness remains conditional on its stated hypotheses. |',
    '| Paper V | The unsupported earlier general endpoint-complete theorem remains withdrawn. The current manuscript proves general polynomial boundary systems and the explicit elliptic fixed-triangle comparison. The October 5 follow-up clarifies observable relative monodromy, supplies a localized fixed-chain comparison proposition, expands the orbit proof, and corrects source pinpoints. Broader multiblock formal completeness remains conditional on its stated hypotheses. |')
replace('notes/repository-status.md',
    '- Paper V: the current fixed-triangle elliptic theorem and its actual polynomial boundary-system formulation replace the withdrawn endpoint-complete claim.',
    '- Paper V: the current fixed-triangle elliptic theorem and its actual polynomial boundary-system formulation replace the withdrawn endpoint-complete claim.\n- Paper V follow-up: source-checked citations, the fixed-base observable hypothesis, the localized actual/specialized-formal distinction, and the expanded affine-orbit proof are integrated. The principal independence statements are unchanged.')
replace('notes/repository-status.md',
    '\n## Detailed records by paper\n',
    '| 2026-10-05 | Paper V audit follow-up | Clarify the actual relative-monodromy hypothesis and localized formal comparison; expand the affine-orbit proof and correct version-specific references without weakening the elliptic independence statements. |\n\n## Detailed records by paper\n')
replace('notes/repository-status.md',
    '| [Repair-session closeout](provenance/repair-session-closeout-2026-09-29.md) | Cross-document dependency review and final scope of the September repair session. |',
    '| [Repair-session closeout](provenance/repair-session-closeout-2026-09-29.md) | Cross-document dependency review and final scope of the September repair session. |\n| [October 5 audit follow-up](provenance/paper-v-audit-followup-2026-10-05.md) | Additional audit of the proposed clarifications, source-to-claim checks, and precise actual versus specialized formal scope. |\n| [Follow-up build verification](provenance/paper-v-audit-followup-build-2026-10-05.json) | Official build, snapshot preservation, and reproducible rendering fingerprints. |')

builddir = Path('.build/paper-v-revision-validation')
builddir.mkdir(parents=True, exist_ok=True)

def run(command, name):
    result = subprocess.run(command, capture_output=True, text=True)
    (builddir / (name + '.txt')).write_text(result.stdout + result.stderr)
    print(name + ': exit ' + str(result.returncode), flush=True)
    if result.returncode:
        print((result.stdout + result.stderr)[-14000:])
        raise RuntimeError(name + ' failed')

base_manifest = json.loads(prior(MANIFEST))
run(['make', 'test'], 'unit-tests')
run(['python3', 'scripts/check_paper_v.py'], 'extended-exact-checks')
run(['make', 'pdf'], 'make-pdf')
new_manifest = json.loads(Path(MANIFEST).read_text())
new_record = next(x for x in new_manifest['documents'] if x['source'] == SOURCE)
assert new_record['source_sha256'] == EXPECTED_SOURCE
records = []
preserved = []
for record in base_manifest['documents']:
    if record['source'] == SOURCE:
        records.append(new_record)
        continue
    assert Path(record['source']).read_bytes() == prior(record['source'])
    Path(record['pdf']).write_bytes(prior(record['pdf']))
    assert digest(Path(record['pdf']).read_bytes()) == record['pdf_sha256']
    records.append(record)
    preserved.append({'source': record['source'], 'source_sha256': record['source_sha256'],
                      'pdf': record['pdf'], 'pdf_sha256': record['pdf_sha256'],
                      'manifest_record_unchanged': True})
assert len(preserved) == 8
Path(MANIFEST).write_text(json.dumps({'schema_version': 1, 'documents': records}, indent=2) + '\n')
run(['make', 'check'], 'make-check')

before = prior(SOURCE).decode()
after = Path(SOURCE).read_text()
assert before.split('\\begin{document}')[0] == after.split('\\begin{document}')[0]
labels_before = re.findall(r'\\label\{([^}]+)\}', before)
labels_after = re.findall(r'\\label\{([^}]+)\}', after)
assert len(labels_after) == len(set(labels_after))
assert set(labels_before) <= set(labels_after)
principal = ['thm:intro-elliptic', 'thm:criterion', 'thm:elliptic-main', 'thm:values']
for label in principal:
    pattern = r'\\label\{' + re.escape(label) + r'\}.*?\\end\{theorem\}'
    assert re.search(pattern, before, re.S).group() == re.search(pattern, after, re.S).group()
keys = re.findall(r'\\bibitem\{([^}]+)\}', after)
cited = set()
for match in re.finditer(r'\\cite(?:\[[^\n]*?\])?\{([^}]+)\}', after):
    cited.update(match[1].split(','))
assert len(keys) == len(set(keys))
assert cited <= set(keys)
assert set(keys) <= cited

pdf_bytes = Path(PDF).read_bytes()
doc = fitz.open(PDF)
text_hashes = []
render_hashes = []
for page in doc:
    text_hashes.append(digest(page.get_text().encode()))
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    render_hashes.append(digest(pix.samples))
text_fingerprint = digest('\n'.join(text_hashes).encode())
render_fingerprint = digest('\n'.join(render_hashes).encode())
logpath = Path('.build/polynomial-flag-exponential-periods/polynomial-flag-exponential-periods.log')
log = logpath.read_text(errors='replace')
warnings = [line for line in log.splitlines() if 'Warning' in line or 'Overfull' in line or 'Underfull' in line]
report = {
    'date': '2026-10-05', 'baseline_commit': BASE,
    'build_input_commit': os.environ['GITHUB_SHA'],
    'workflow_run': 'https://github.com/' + os.environ['GITHUB_REPOSITORY'] + '/actions/runs/' + os.environ['GITHUB_RUN_ID'],
    'platform': 'ubuntu-24.04',
    'commands_passed': ['make test', 'python3 scripts/check_paper_v.py', 'make pdf', 'make check'],
    'unit_test_methods': 11,
    'extended_exact_checks': json.loads(Path('.build/paper-v-exact-checks.json').read_text()),
    'paper_v': {'source': SOURCE, 'source_sha256': digest(Path(SOURCE).read_bytes()),
                'pdf': PDF, 'pdf_sha256': digest(pdf_bytes), 'pages': len(doc),
                'log_sha256': digest(logpath.read_bytes()), 'log_diagnostics': warnings},
    'preservation': {'principal_statements_unchanged': principal,
                     'preamble_authorship_title_contact_date_unchanged': True,
                     'all_original_labels_retained': True,
                     'original_labels': len(labels_before), 'current_labels': len(labels_after),
                     'bibliography_entries': len(keys), 'all_entries_cited': True,
                     'other_eight_pairs': preserved},
    'render_verification': {'pymupdf_version': fitz.VersionBind, 'dpi': 108,
                            'text_hashes': text_hashes, 'render_rgb_hashes': render_hashes,
                            'text_fingerprint': text_fingerprint, 'render_fingerprint': render_fingerprint,
                            'locally_inspected_text_fingerprint': LOCAL_TEXT,
                            'locally_inspected_render_fingerprint': LOCAL_RENDER,
                            'matches_locally_inspected_text': text_fingerprint == LOCAL_TEXT,
                            'matches_locally_inspected_render': render_fingerprint == LOCAL_RENDER},
    'limits': 'Build and finite exact checks are not independent peer review or formal verification. Final clean-tree PR and post-merge CI are recorded in the pull-request discussion.'
}
Path(REPORT).write_text(json.dumps(report, indent=2) + '\n')
allowed = {SOURCE, PDF, MANIFEST, 'README.md', 'notes/repository-status.md', NOTE, REPORT}
changed = set(subprocess.check_output(['git', 'diff', '--name-only', BASE], text=True).splitlines())
helpers = {'scripts/_paper_v_revision_patch.py', 'scripts/_paper_v_revision_delivery.py', '.github/workflows/paper-v-revision.yml'}
assert changed <= allowed | helpers, changed
for path in sorted(allowed):
    subprocess.run(['git', 'add', '--', path], check=True)
subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
subprocess.run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
subprocess.run(['git', 'commit', '-m', 'Paper V: source-checked follow-up, localized comparison, and verified PDF'], check=True)
subprocess.run(['git', 'push', 'origin', 'HEAD:refs/heads/' + BRANCH], check=True)
print(json.dumps({'source_sha256': EXPECTED_SOURCE, 'pages': len(doc), 'text_match': text_fingerprint == LOCAL_TEXT, 'render_match': render_fingerprint == LOCAL_RENDER, 'commit': subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}, indent=2))
