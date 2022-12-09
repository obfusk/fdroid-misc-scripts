#!/bin/bash
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8
mkdir -p apps
echo 'getting apps from index-v1.json...'
jq -r '.apps[].packageName' < index-v1.json | sort > apps/index-apps
echo 'listing apps from metadata...'
(
  cd fdroiddata/metadata
  ls *.yml
) | sed 's!\.yml$!!' | sort > apps/metadata-apps
(
  cd fdroiddata/metadata
  grep -lE '^ArchivePolicy: 0|^Disabled:' *.yml
) | sed 's!\.yml$!!' | sort > apps/metadata-apps-archived-and-disabled
echo 'diffing...'
diff -Naur apps/metadata-apps apps/metadata-apps-archived-and-disabled \
  | grep ^- | cut -c2- | tail -n +2 > apps/metadata-apps-not-archived-or-disabled
diff -Naur apps/index-apps apps/metadata-apps-not-archived-or-disabled \
  | grep ^- | cut -c2- | tail -n +2 > apps/index-apps-not-in-metadata
diff -Naur apps/index-apps apps/metadata-apps-not-archived-or-disabled \
  | grep ^+ | cut -c2- | tail -n +2 > apps/metadata-apps-not-in-index
