#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
if [ $# = 0 ]; then
  blks=( fdroiddata/metadata/*/signatures/*/APKSigningBlock )
else
  blks=( "$@" )
fi
for blk in "${blks[@]}"; do
  blocks=( $( apksigtool parse --json --block "$blk" 2>/dev/null \
                | jq -r '.pairs[].value._type' \
                | grep -Ev '^(APKSignatureSchemeBlock|VerityPaddingBlock)$' || true ) )
  if [ "${#blocks[@]}" != 0 ]; then
    echo "$blk: ${blocks[@]}"
  fi
done
