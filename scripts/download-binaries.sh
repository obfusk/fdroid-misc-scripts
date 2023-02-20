#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
mkdir -p binaries
for yml in $( grep -lE '^Binaries|^    binary: http' \
                fdroiddata/metadata/*.yml | sort ); do
  echo "==> $yml"
  base="$( basename "$yml" .yml )"
  read -r version code upstream_url < <( python3 -c '
import sys, yaml
with open(sys.argv[1]) as fh:
    m = yaml.safe_load(fh.read())
bins = m.get("Binaries")
for b in reversed(m["Builds"]):
    if not "disable" in b:
        v = b["versionName"]
        c = b["versionCode"]
        bin = b.get("binary", bins)
        print(v, c, bin.replace("%v", v).replace("%c", str(c)))
        break
else:
    print()
' "$yml" )
  if [ -z "$version" -o -z "$code" ]; then
    echo 'all versions disabled'
  else
    echo "version=$version code=$code"
    upstream="binaries/${base}_${code}_upstream.apk"
    fdroid="binaries/${base}_${code}_fdroid.apk"
    fdroid_url="https://f-droid.org/repo/${base}_${code}.apk"
    [ -e "$upstream" ] || wget -O "$upstream" -- "$upstream_url" \
      || { echo 'not found upstream'; rm "$upstream"; }
    [ -e "$fdroid" ] || wget -O "$fdroid" -- "$fdroid_url" \
      || { echo 'not found in f-droid'; rm "$fdroid"; }
  fi
  echo
done
