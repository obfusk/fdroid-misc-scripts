#!/bin/bash
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8

verification="$( readlink -f verification )"

apks_from_index() {
  python3 -c '
import json, sys
apks = {}
with open("repo/index-v1.json") as fh:
    idx_data = json.load(fh)
for appid, apk_data in sorted(idx_data["packages"].items()):
    apks[appid] = sorted(set(x["apkName"] for x in apk_data))
json.dump(apks, sys.stdout, indent=2, sort_keys=True)
'
}

pushd f-droid.org-transparency-log
git status
if [ -n "$1" ]; then
  date="$1"
  commit="$( git log --pretty='%H %ad' --date=format:%F \
               | grep -F "$date" | tail -1 | cut -d' ' -f1 )"
  echo "checking out $commit^..."
  git checkout "$commit^"
else
  date="$( date +%F )"
fi
echo "date=$date"
if [[ "$date" = *- ]]; then
  date="${date}01"
fi
echo "writing index-apks-$date.json..."
apks_from_index > "$verification/index-apks-$date.json"
if [ -n "$1" ]; then
  echo "checking out master..."
  git checkout master
fi
popd # f-droid.org-transparency-log
