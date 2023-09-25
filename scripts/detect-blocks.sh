#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
if [ $# = 0 ]; then
  apks=( *.apk )
else
  apks=( "$@" )
fi
for apk in "${apks[@]}"; do
  # shellcheck disable=SC2207
  blocks=( $( apksigtool parse --json "$apk" 2>/dev/null \
                | jq -r '.pairs[].value._type' \
                | grep -Ev '^(APKSignatureSchemeBlock|VerityPaddingBlock)$' || true ) )
  if [ "${#blocks[@]}" != 0 ]; then
    echo "$apk:" "${blocks[@]}"
  fi
done
