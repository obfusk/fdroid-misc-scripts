#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
zfe_sha1=7170680469ab42a97fe39d10011c5b72971a57a4
for apk in *.apk; do
  if [ "$( head -c28 "$apk" | shasum | cut -c-40 )" = "$zfe_sha1" ]; then
    echo "$apk"
  fi
done
