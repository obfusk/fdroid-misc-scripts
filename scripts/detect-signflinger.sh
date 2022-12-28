#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
for apk in *.apk; do
  if [ "$( apksigtool parse-v1 --json "$apk" 2>/dev/null \
             | jq -r .manifest.built_by )" = Signflinger ]; then
    echo "$apk"
  fi
done
