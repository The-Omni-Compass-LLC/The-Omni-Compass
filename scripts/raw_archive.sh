#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The raw receipts of every archived run live on the branch `raw` (18 October): its root holds what results/live/raw/
# held on main (run-<id>/, addons-run-<id>/, capacity-run-<id>/, ...), byte for byte, with every SHA256SUMS file. Main's
# tree is the code and the tables, so a clone of main (Dependabot's, a buyer's, a runner's) no longer carries 36 GB of
# receipts: Dependabot's every clone had timed out after 15 minutes. Opened, the branch sits at results/live/raw/ as a
# worktree, so every path a page or a tool names (results/live/raw/run-<id>/...) reads as before. Only trees are fetched;
# a file is downloaded when a checkout asks for it.
# Usage (from the repository's root):
#   scripts/raw_archive.sh fetch               the branch's newest commit, trees only (origin/raw)
#   scripts/raw_archive.sh open [PATTERN...]   results/live/raw/ as a worktree of the branch with only these folders
#                                              checked out (run-<id>/, or a pattern such as /*/redis-*/); none: nothing
#   scripts/raw_archive.sh has DIR             exit 0 when the branch holds DIR (run-<id>), from trees only
#   scripts/raw_archive.sh save DIR MESSAGE    commit results/live/raw/DIR to the branch and push it (built from trees on
#                                              the branch's newest tip, so a branch that moved is never a conflict)
#   scripts/raw_archive.sh sweep               move every folder main's HEAD still carries under results/live/raw/ to the
#                                              branch (trees only, nothing downloaded), then take it out of main's tree;
#                                              RAW_SWEEP_PUSH=0 commits on main without pushing
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
W=results/live/raw
REMOTE="${RAW_REMOTE:-origin}"
REF="refs/remotes/$REMOTE/raw"

fetch() {
  local i
  for i in 1 2 3 4; do
    if git ls-remote --exit-code "$REMOTE" refs/heads/raw >/dev/null 2>&1; then
      git fetch -q --depth=1 --filter=blob:none "$REMOTE" "+refs/heads/raw:$REF" && return 0
    else
      return 0                                   # no branch yet: the first sweep makes it
    fi
    sleep $((2 ** i))
  done
  echo "raw archive: the branch could not be fetched" >&2; return 1
}

is_worktree() { [ -e "$W/.git" ]; }

open() {
  fetch
  git rev-parse -q --verify "$REF" >/dev/null || { echo "raw archive: no branch raw yet" >&2; return 1; }
  if ! is_worktree; then
    local aside=""
    if [ -d "$W" ] && [ -n "$(ls -A "$W" 2>/dev/null)" ]; then  # files written before the branch was opened: kept, put back
      aside=$(mktemp -d); cp -a "$W/." "$aside/"
    fi
    rm -rf "$W"
    git worktree prune
    git worktree add -q --no-checkout --detach -f "$W" "$REF"
    git -C "$W" sparse-checkout set --no-cone '!/*'
    git -C "$W" checkout -q
    [ -z "$aside" ] || { cp -a "$aside/." "$W/"; rm -rf "$aside"; }
  fi
  if [ "$#" -gt 0 ]; then
    git -C "$W" sparse-checkout add "$@"
  fi
}

has() { fetch; git cat-file -e "$REF:$1" 2>/dev/null; }

ID=(-c "user.name=${GIT_AUTHOR_NAME:-github-actions[bot]}" -c "user.email=${GIT_AUTHOR_EMAIL:-41898282+github-actions[bot]@users.noreply.github.com}")

# a tree holding the root's entries with one name set to a tree (trees only: no history, no file downloaded)
with_entry() {   # ROOT_TREE_OR_EMPTY NAME TREE
  { [ -z "$1" ] || git ls-tree "$1" | awk -F'\t' -v n="$2" '$2 != n'; printf '040000 tree %s\t%s\n' "$3" "$2"; } | git mktree
}

save() {
  local dir="$1" msg="$2" idx dir_tree root new_tree commit i
  [ -d "$W/$dir" ] || { echo "raw archive: $W/$dir does not exist" >&2; return 1; }
  # the folder's own tree, from a private index over results/live/raw/ (main's index and sparse rules untouched)
  idx=$(mktemp); rm -f "$idx"
  GIT_INDEX_FILE="$idx" git -c core.sparseCheckout=false --work-tree="$W" add -f -- "$dir"
  dir_tree=$(GIT_INDEX_FILE="$idx" git --work-tree="$W" write-tree --prefix="$dir/")
  rm -f "$idx"
  for i in 1 2 3 4 5 6; do
    fetch
    root=$(git rev-parse -q --verify "$REF^{tree}" 2>/dev/null || true)
    if [ -n "$root" ] && [ "$(git rev-parse -q --verify "$REF:$dir" 2>/dev/null)" = "$dir_tree" ]; then
      echo "raw archive: $dir is already on the branch, unchanged"; return 0
    fi
    new_tree=$(with_entry "$root" "$dir" "$dir_tree")
    if [ -n "$root" ]; then commit=$(git "${ID[@]}" commit-tree "$new_tree" -p "$REF" -m "$msg")
    else commit=$(git "${ID[@]}" commit-tree "$new_tree" -m "$msg"); fi
    git push -q "$REMOTE" "$commit:refs/heads/raw" && { echo "raw archive: $dir saved"; return 0; }
    echo "raw archive: the branch moved (attempt $i); building on its new tip" >&2
    sleep $((5 * i))
  done
  echo "raw archive: $dir could not be pushed after six attempts" >&2; return 1
}

sweep() {
  local main_tree raw_tree new_tree commit i
  main_tree=$(git rev-parse -q --verify "HEAD:$W" 2>/dev/null) || { echo "raw archive: main carries no raw folder"; return 0; }
  for i in 1 2 3 4 5 6; do
    fetch
    raw_tree=$(git rev-parse -q --verify "$REF^{tree}" 2>/dev/null || true)
    # the union of the two trees by folder name; where both hold a name with different contents, main's copy is kept
    # beside the branch's under the name <name>.main-<first 8 of its id>, so nothing is ever dropped
    new_tree=$( { [ -z "$raw_tree" ] || git ls-tree "$raw_tree" | sed 's/^/R /'; git ls-tree "$main_tree" | sed 's/^/M /'; } \
      | awk -F'\t' '{split($1, a, " "); src=a[1]; meta=a[2] " " a[3] " " a[4]; name=$2
                     if (src == "R") { have[name]=a[4]; print meta "\t" name; next }
                     if (!(name in have)) { print meta "\t" name; next }
                     if (have[name] != a[4]) print meta "\t" name ".main-" substr(a[4], 1, 8) }' \
      | git mktree)
    if [ "$new_tree" != "$raw_tree" ]; then
      if [ -n "$raw_tree" ]; then
        commit=$(git "${ID[@]}" commit-tree "$new_tree" -p "$REF" -m "Raw receipts moved from main's tree to the branch raw")
      else
        commit=$(git "${ID[@]}" commit-tree "$new_tree" -m "The raw receipts of every archived run, moved from main's tree (results/live/raw/) to their own branch")
      fi
      git push -q "$REMOTE" "$commit:refs/heads/raw" || { echo "raw archive: the branch moved (attempt $i)" >&2; sleep $((5 * i)); continue; }
      fetch
    fi
    # every folder main carries is now on the branch, under its own name or beside it: only then leave main's tree
    git ls-tree --name-only "$main_tree" | while IFS= read -r n; do
      git cat-file -e "$REF:$n" 2>/dev/null || { echo "raw archive: $n is not on the branch; main keeps it" >&2; exit 1; }
    done
    git rm -r -q --cached --sparse "$W"
    git "${ID[@]}" commit -q -m "Raw receipts moved to the branch raw (scripts/raw_archive.sh): main's tree is the code and the tables"
    [ "${RAW_SWEEP_PUSH:-1}" = 1 ] || { echo "raw archive: moved; main committed, not pushed"; return 0; }
    for i in 1 2 3 4 5 6; do
      git push -q "$REMOTE" HEAD && { echo "raw archive: moved; main pushed"; return 0; }
      sleep $((5 * i)); git pull -q --rebase "$REMOTE" "$(git rev-parse --abbrev-ref HEAD)"
    done
    echo "raw archive: main could not be pushed; the branch already holds everything" >&2; return 1
  done
  echo "raw archive: the branch could not be updated after six attempts" >&2; return 1
}

cmd="${1:-}"; shift || true
case "$cmd" in
  fetch) fetch ;;
  open) open "$@" ;;
  has) has "$1" ;;
  save) save "$1" "$2" ;;
  sweep) sweep ;;
  *) sed -n '7,25p' "$0"; exit 2 ;;
esac
