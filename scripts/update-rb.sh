#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8

process_with_python() {
  python3 -c '
import sys
with open("disabled") as fh:
    disabled = set(l.strip() for l in fh.readlines())
with open("missing") as fh:
    missing = set(l.strip() for l in fh.readlines())
with open("no-longer-rb") as fh:
    no_longer_rb = set(l.strip() for l in fh.readlines())
with open("signflinger") as fh:
    signflinger = set(l.strip() for l in fh.readlines())
for line in sys.stdin:
    appid = line.strip()
    info = []
    if appid in disabled:
        info.append("disabled")
    if appid in missing:
        info.append("missing")
    if appid in no_longer_rb:
        info.append("no longer RB")
    if appid in signflinger:
        info.append("signflinger")
    if i := ", ".join(info):
        print(f"{appid} [{i}]")
    else:
        print(appid)
'
}

pushd fdroiddata
git status
if [ -n "$1" ]; then
  date="$1"
  commit="$( git log --pretty='%H %cd' --date=format:%F \
               | grep -F "$date" | tail -1 | cut -d' ' -f1 )"
  echo "checking out $commit..."
  git checkout "$commit"
else
  date="$( date +%F )"
fi
echo "date=$date"
echo 'listing Binaries...'
binaries="$( grep -l ^Binaries: metadata/*.yml | sort \
               | sed -r 's!^metadata/!!; s!\.yml$!!' )"
echo 'listing signatures...'
signatures="$( ls -d metadata/*/signatures | sort \
                 | sed -r 's!^metadata/!!; s!/signatures$!!')"
if [ -n "$1" ]; then
  echo "checking out master..."
  git checkout master
fi
popd # fdroiddata

pushd reproducible
echo "writing $date-bins..."
printf '%s\n' "$binaries" | process_with_python > "$date-bins"
echo "writing $date-sigs..."
printf '%s\n' "$signatures" | process_with_python > "$date-sigs"
popd # reproducible
