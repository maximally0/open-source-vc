#!/usr/bin/env bash
#
# Clone curated projects to your own machine.
#
# This repository deliberately does not vendor third-party source code
# (see docs/LOCAL_COPIES.md). This script is how you get the code locally
# instead — into ./clones/, which is git-ignored.
#
# Usage:
#   ./scripts/clone_repos.sh                          # everything
#   ./scripts/clone_repos.sh --tier essential         # one tier
#   ./scripts/clone_repos.sh --category legal         # one category
#   ./scripts/clone_repos.sh --shallow --tier essential
#   ./scripts/clone_repos.sh --list                   # show what would be cloned
#   ./scripts/clone_repos.sh --dest /some/path
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
META="$ROOT/metadata/repositories.json"
DEST="$ROOT/clones"
TIER=""
CATEGORY=""
SHALLOW=0
LIST_ONLY=0

while [ $# -gt 0 ]; do
  case "$1" in
    --tier)      TIER="${2:-}"; shift 2 ;;
    --category)  CATEGORY="${2:-}"; shift 2 ;;
    --dest)      DEST="${2:-}"; shift 2 ;;
    --shallow)   SHALLOW=1; shift ;;
    --list)      LIST_ONLY=1; shift ;;
    -h|--help)   sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

if [ ! -f "$META" ]; then
  echo "error: $META not found. Run 'python scripts/generate_index.py' first." >&2
  exit 1
fi

if ! command -v python >/dev/null 2>&1; then
  echo "error: python is required to read the metadata." >&2
  exit 1
fi

# Emit "name<TAB>tier<TAB>category<TAB>license" rows, filtered.
rows=$(python - "$META" "$TIER" "$CATEGORY" <<'PY'
import json, sys
meta, tier, category = sys.argv[1], sys.argv[2].lower(), sys.argv[3].lower()
data = json.load(open(meta, encoding="utf-8"))
for r in data.get("repositories", []):
    if tier and (r.get("tier") or "").lower() != tier:
        continue
    if category and (r.get("category") or "").lower() != category:
        continue
    print("\t".join([r["name"], r.get("tier", ""), r.get("category", ""), r.get("license", "unknown")]))
PY
)

if [ -z "$rows" ]; then
  echo "No projects matched. Check --tier / --category against metadata/repositories.json."
  exit 0
fi

total=$(printf '%s\n' "$rows" | wc -l | tr -d ' ')

if [ "$LIST_ONLY" -eq 1 ]; then
  printf '%s\n' "$rows" | while IFS=$'\t' read -r name tier category license; do
    printf '%-45s %-15s %-25s %s\n' "$name" "$tier" "$category" "$license"
  done
  echo "---"
  echo "$total project(s)"
  exit 0
fi

echo "Cloning $total project(s) into $DEST"
echo "Licences are printed as each clone starts. Respect them when you reuse code."
echo

ok=0
failed=0

while IFS=$'\t' read -r name tier category license; do
  safe_category=$(printf '%s' "$category" | tr -c 'a-zA-Z0-9._-' '-')
  target="$DEST/$safe_category/$(basename "$name")"

  if [ -d "$target/.git" ]; then
    printf '%-45s already present, skipping\n' "$name"
    ok=$((ok + 1))
    continue
  fi

  mkdir -p "$(dirname "$target")"
  printf '%-45s %-14s %s\n' "$name" "$license" "$target"

  if [ "$SHALLOW" -eq 1 ]; then
    if git clone --depth 1 --quiet "https://github.com/$name.git" "$target" 2>/dev/null; then
      ok=$((ok + 1))
    else
      echo "    ! clone failed: $name"
      failed=$((failed + 1))
    fi
  else
    if git clone --quiet "https://github.com/$name.git" "$target" 2>/dev/null; then
      ok=$((ok + 1))
    else
      echo "    ! clone failed: $name"
      failed=$((failed + 1))
    fi
  fi
done <<< "$rows"

echo
echo "done: $ok cloned, $failed failed"
echo "location: $DEST  (git-ignored — nothing here can be committed)"
