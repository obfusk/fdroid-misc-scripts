#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
scripts="$( readlink -f scripts )"
(
  cd binaries
  "$scripts"/detect-virtual-entry.sh \
    | sed -r 's/_[0-9]+_(fdroid|upstream)\.apk$//' | sort | uniq
) > reproducible/signflinger
