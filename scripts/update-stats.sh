#!/bin/bash
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8

pushd fdroiddata
git status
if [ -n "$1" ]; then
  date="$1"
  commit="$( git log --pretty='%H %cd' --date=format:%F \
               | grep -F "$date" | tail -1 | cut -d' ' -f1 )"
  echo "checking out $commit^..."
  git checkout "$commit^"
else
  date="$( date +%F )"
fi
echo "date=$date"
echo 'listing apps...'
# shellcheck disable=SC2207,SC2035
apps=( $( cd metadata && grep -LE '^ArchivePolicy: 0|^Disabled:' *.yml \
            | sed 's!\.yml$!!' | sort ) )
if [ -n "$1" ]; then
  echo "checking out master..."
  git checkout master
fi
popd # fdroiddata

pushd stats
echo "writing $date-apps..."
for app in "${apps[@]}"; do
  printf '%s\n' "$app"
done > "$date-apps"
popd # stats
