#!/usr/bin/env python3
"""Move README entries whose repo has not been pushed to in 12 months into LEGACY.md.

Usage: python3 legacy_split.py [README.md] [LEGACY.md]
Auth:  GITHUB_TOKEN env var, else `gh auth token`. Unauthenticated limit (60/h) is too low for ~120 repos.
Rows without a last-commit badge (orgs, non-GitHub) are kept in README.
Repos the API cannot resolve (404 etc.) are kept and reported.
"""
import json, os, re, subprocess, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

ROW = re.compile(r"^\|.*last-commit/([^/\s)]+/[^/\s)]+)\)")
HEAD = re.compile(r"^(#{2,6}) (.+)$")
DAYS = 365


def token():
    t = os.environ.get("GITHUB_TOKEN")
    if t:
        return t
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    except Exception:
        return None


def pushed_at(repo, tok):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": "legacy-split"})
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        return datetime.fromisoformat(d["pushed_at"].replace("Z", "+00:00"))
    except urllib.error.HTTPError as e:
        print(f"WARN {repo}: HTTP {e.code}, kept", file=sys.stderr)
    except Exception as e:
        print(f"WARN {repo}: {e}, kept", file=sys.stderr)
    return None


def anchor(title):
    a = re.sub(r"[^\w\s-]", "", title.lower()).strip()
    return re.sub(r"\s", "-", a)


def split(lines, dates, cutoff):
    keep, legacy = [], []  # legacy: (heading_stack, row, date)
    stack = []
    for ln in lines:
        m = HEAD.match(ln)
        if m:
            lvl = len(m.group(1))
            stack = [h for h in stack if h[0] < lvl] + [(lvl, m.group(2))]
        r = ROW.match(ln)
        if r and dates.get(r.group(1)) and dates[r.group(1)] < cutoff:
            legacy.append((list(stack), ln, dates[r.group(1)]))
        else:
            keep.append(ln)
    return keep, legacy


def prune(lines):
    """Drop tables with no data rows, then headings (level>=3) with nothing under them."""
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("| Project Name") and i + 1 < len(lines) and lines[i + 1].startswith("| :---"):
            j = i + 2
            if not (j < len(lines) and lines[j].startswith("|")):
                i = j
                continue
        out.append(lines[i])
        i += 1
    # remove empty h3+ blocks (repeat until stable)
    changed = True
    while changed:
        changed = False
        idx = [(k, len(HEAD.match(l).group(1))) for k, l in enumerate(out) if HEAD.match(l)]
        for n, (k, lvl) in enumerate(idx):
            end = idx[n + 1][0] if n + 1 < len(idx) else len(out)
            body = [l for l in out[k + 1:end] if l.strip() and not l.startswith(">")]
            nxt_lvl = idx[n + 1][1] if n + 1 < len(idx) else 0
            if lvl >= 3 and not body and nxt_lvl <= lvl:
                del out[k:end]
                changed = True
                break
    return out


def fix_contents(lines):
    anchors = {anchor(HEAD.match(l).group(2)) for l in lines if HEAD.match(l)}
    res = []
    for l in lines:
        if l.startswith("| [") and "](#" in l and "|" in l[1:]:
            cells = l.split(" | ")
            if len(cells) >= 2:
                subs = [s for s in cells[1].rstrip(" |").split(" · ") if s.strip()]
                kept = [s for s in subs if not re.match(r"\[.*\]\(#(.+)\)", s.strip()) or
                        re.match(r"\[.*\]\(#(.+)\)", s.strip()).group(1) in anchors]
                cells[1] = (" · ".join(kept) if kept else "") + " |"
                l = " | ".join(cells[:2])
        res.append(l)
    return res


def write_legacy(path, legacy, today):
    out = ["# Legacy", "",
           f"Repositories with no push in the 12 months before {today:%d %B %Y}, moved out of the main list.", ""]
    last = None
    for stack, row, d in legacy:
        key = tuple(stack)
        if key != last:
            common = 0
            while last and common < min(len(last), len(key)) and last[common] == key[common]:
                common += 1
            for lvl, title in key[common:]:
                out += ["", "#" * lvl + " " + title]
            out += ["", "| Project Name | Description | Last push |", "| :--- | :--- | :--- |"]
            last = key
        out.append(row.rstrip().rstrip("|").rstrip() + f" | {d:%Y-%m-%d} |")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")


def main(readme="README.md", legacy_path="LEGACY.md", fetch=None, now=None):
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=DAYS)
    lines = open(readme, encoding="utf-8").read().split("\n")
    repos = sorted({ROW.match(l).group(1) for l in lines if ROW.match(l)})
    tok = None if fetch else token()
    dates = {r: (fetch or (lambda x: pushed_at(x, tok)))(r) for r in repos}
    keep, legacy = split(lines, dates, cutoff)
    keep = fix_contents(prune(keep))
    open(readme, "w", encoding="utf-8").write("\n".join(keep))
    write_legacy(legacy_path, legacy, now)
    print(f"{len(repos)} repos checked, {len(legacy)} moved to {legacy_path}, "
          f"{sum(1 for v in dates.values() if v is None)} unresolved (kept)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
