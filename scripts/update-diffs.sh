#!/bin/bash
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
set -e
export LC_ALL=C.UTF-8

pushd stats
files=( *-apps )
i=0 l=${#files[@]}
while (( i < l - 1 )); do
  j=$(( i + 1 ))
  x="${files[i]}" y="${files[j]}"
  z="${y%-apps}"
  diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$z"-rems
  diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$z"-adds
  (( ++i ))
done
popd # stats

pushd reproducible
files=( *-bins )
i=0 l=${#files[@]}
while (( i < l - 1 )); do
  j=$(( i + 1 ))
  x="${files[i]}" y="${files[j]}"
  diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$y"-rems
  diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$y"-adds
  (( ++i ))
done
files=( *-sigs )
i=0 l=${#files[@]}
while (( i < l - 1 )); do
  j=$(( i + 1 ))
  x="${files[i]}" y="${files[j]}"
  diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$y"-rems
  diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$y"-adds
  (( ++i ))
done
popd # reproducible
