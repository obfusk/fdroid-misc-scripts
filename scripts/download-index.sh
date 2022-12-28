#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
wget -O index-v1.jar -- https://f-droid.org/repo/index-v1.jar
if [ -x "$( command -v apksigtool )" ]; then
  apksigtool verify-v1 --allow-unsafe=SHA1 \
    --signed-by=43238d512c1e5eb2d6569f4a3afbf5523418b82e0a3ed1552770abb9a9c9ccab: index-v1.jar
else
  echo 'WARNING: apksigtool not found; unable to verify JAR' >&2
  read -r -p "Continue without verification? "
  [[ "$REPLY" == [Yy]* ]] || exit 1
fi
unzip -o index-v1.jar index-v1.json
