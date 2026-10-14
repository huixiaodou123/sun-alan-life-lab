#!/usr/bin/env python3
"""Record verified source deltas and precise module edits in a writable Skill copy."""
import argparse
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

MARKER = '\n## 增量核对记录\n'


def digest(value):
    raw = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


def canonical(url):
    p = urlsplit(url)
    if p.scheme not in ('http', 'https') or not p.netloc or p.username or p.password:
        raise ValueError('url must be a public HTTP(S) source without embedded credentials')
    q = [(k, v) for k, v in parse_qsl(p.query) if not k.startswith('utm_')]
    return urlunsplit((p.scheme, p.netloc.lower(), p.path.rstrip('/'), urlencode(q), ''))


def apply(root, record, checked_at):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', checked_at):
        raise ValueError('checked-at must use YYYY-MM-DD')
    for key in ('url', 'author', 'title', 'kind', 'coverage', 'summary', 'impact'):
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError(f'missing nonempty field: {key}')
    if record['kind'] not in ('original', 'community', 'meme'):
        raise ValueError('invalid source kind')
    if record['coverage'] not in ('title', 'description', 'transcript', 'full'):
        raise ValueError('invalid coverage')
    url = canonical(record['url'])
    index_path = root / 'references/update-index.json'
    index = json.loads(index_path.read_text()) if index_path.exists() else {'schema': 1, 'records': []}
    entry = {k: record.get(k) for k in ('author', 'title', 'published_at', 'kind', 'coverage', 'summary', 'impact')}
    entry['url'] = url
    signature = digest({"entry": entry, "module_changes": record.get("module_changes", [])})
    existing = next((e for e in index['records'] if e['url'] == url), None)
    duplicate = existing is not None and existing['fingerprint'] == signature
    changes = record.get('module_changes', [])
    if changes and record['coverage'] not in ('description', 'transcript', 'full'):
        raise ValueError('title-only sources cannot change practice modules')
    staged = {}
    edits = []
    if not duplicate:
        for change in changes:
            rel = Path(change['path'])
            target = (root / rel).resolve()
            refs = (root / 'references').resolve()
            if target.parent != refs or target.suffix != '.md' or not target.is_file():
                raise ValueError('module changes must target existing references/*.md')
            if rel.name in ('sources.md', 'latest-updates.md', 'updates.md'):
                raise ValueError('generated/update control files cannot be module patch targets')
            before, after = change['before'], change['after']
            current = staged.get(target, target.read_text())
            if not before or not after or current.count(before) != 1:
                raise ValueError('module patch must have one exact old paragraph and a nonempty replacement')
            revised = current.replace(before, after, 1)
            staged[target] = revised
            edits.append({'path': str(rel), 'before_sha256': digest(current), 'after_sha256': digest(revised)})
        if existing:
            history = existing.get('history', []) + [{k: v for k, v in existing.items() if k != 'history'}]
            entry['history'] = history
            index['records'].remove(existing)
        entry.update({'fingerprint': signature, 'checked_at': checked_at, 'module_changes': edits})
        index['records'].append(entry)
    else:
        existing['checked_at'] = checked_at
    index['last_checked_at'] = checked_at
    lines = ['# 最近的增量核对', '', '只记录实际读取的新增或修订；只有标题的材料不修改实践规则。', '']
    for e in index['records']:
        lines += [f'## {e["checked_at"]} · {e["title"]}', '', f'- 作者：{e["author"]}；归属：{e["kind"]}；覆盖：{e["coverage"]}。', f'- 来源：{e["url"]}', f'- 发布日期：{e.get("published_at") or "未知"}。', f'- 已读摘要：{e["summary"]}', f'- 对现有 Skill 的影响：{e["impact"]}', f'- 模块修改：{", ".join(c["path"] for c in e.get("module_changes", [])) or "本条仅更新来源/线索，没有自动改实践规则"}。', '']
    latest = '\n'.join(lines)
    sources = root / 'references/sources.md'
    core = sources.read_text().split(MARKER)[0]
    staged[sources] = core + MARKER + '\n详见 [latest-updates.md](latest-updates.md)；记录索引见 [update-index.json](update-index.json)。\n'
    staged[root / 'references/latest-updates.md'] = latest
    staged[index_path] = json.dumps(index, ensure_ascii=False, indent=2) + '\n'
    originals = {f: f.read_bytes() if f.exists() else None for f in staged}
    written = []
    try:
        for f, text in staged.items():
            with tempfile.NamedTemporaryFile(dir=f.parent, mode='w', encoding='utf-8', delete=False) as tmp:
                tmp.write(text); temp = Path(tmp.name)
            try:
                os.replace(temp, f); written.append(f)
            finally:
                temp.unlink(missing_ok=True)
    except Exception:
        for f in written:
            if originals[f] is None:
                f.unlink(missing_ok=True)
            else:
                f.write_bytes(originals[f])
        raise
    return {'status': 'already_recorded' if duplicate else 'recorded', 'url': url, 'module_edits': len(edits), 'checked_at': checked_at}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--checked-at', required=True)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    result = apply(args.root.resolve(), json.loads(args.input.read_text()), args.checked_at)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
