#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
zfe_base64=UEsDBAAAAAAAACEIIQIAAAAAAAAAAAAAAAAAAA==
if [ $# = 0 ]; then
  apks=( *.apk )
else
  apks=( "$@" )
fi
for apk in "${apks[@]}"; do
  if [ "$( head -c28 "$apk" | base64 )" = "$zfe_base64" ]; then
    echo "$apk"
  fi
done
