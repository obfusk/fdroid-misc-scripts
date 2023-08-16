#!/bin/bash
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
key=43238d512c1e5eb2d6569f4a3afbf5523418b82e0a3ed1552770abb9a9c9ccab

mkdir -p v2/{archive,repo}
wget -O v2/repo/entry.jar -- https://f-droid.org/repo/entry.jar
wget -O v2/archive/entry.jar -- https://f-droid.org/archive/entry.jar
wget -O v2/repo/index-v2.json -- https://f-droid.org/repo/index-v2.json
wget -O v2/archive/index-v2.json -- https://f-droid.org/archive/index-v2.json

if [ -x "$( command -v apksigtool )" ]; then
  apksigtool verify-v1 --signed-by="$key": v2/repo/entry.jar
  apksigtool verify-v1 --signed-by="$key": v2/archive/entry.jar
else
  echo 'WARNING: apksigtool not found; unable to verify JAR' >&2
  read -r -p "Continue without verification? "
  [[ "$REPLY" == [Yy]* ]] || exit 1
fi

pushd v2/repo
unzip -o entry.jar entry.json
shasum="$( jq -r .index.sha256 < entry.json )"
sha256sum -c <<< "$shasum  index-v2.json"
popd
pushd v2/archive
unzip -o entry.jar entry.json
shasum="$( jq -r .index.sha256 < entry.json )"
sha256sum -c <<< "$shasum  index-v2.json"
popd
