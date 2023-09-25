#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
if [ $# = 0 ]; then
  compare=( apksigcopier compare )
else
  compare=( "$@" )
fi
# shellcheck disable=SC2012
for apk in $( ls | sed -r 's/_(fdroid|upstream)\.apk$//' | sort | uniq ); do
  printf '%-71s ' "$apk"
  if [ -e "${apk}_upstream.apk" ] && [ -e "${apk}_fdroid.apk" ]; then
    if "${compare[@]}" "${apk}_upstream.apk" "${apk}_fdroid.apk"; then
      echo OK
    else
      echo FAILED
    fi
  else
    echo skipped
  fi
done
