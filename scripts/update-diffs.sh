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
  if [ -e "$z"-rems ]; then
    echo "skipping $z-rems"
  else
    echo "creating $z-rems..."
    diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$z"-rems
  fi
  if [ -e "$z"-adds ]; then
    echo "skipping $z-adds"
  else
    echo "creating $z-adds..."
    diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$z"-adds
  fi
  (( ++i ))
done
popd # stats

pushd reproducible
files=( *-bins )
i=0 l=${#files[@]}
while (( i < l - 1 )); do
  j=$(( i + 1 ))
  x="${files[i]}" y="${files[j]}"
  if [ -e "$y"-rems ]; then
    echo "skipping $y-rems"
  else
    echo "creating $y-rems..."
    diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$y"-rems
  fi
  if [ -e "$y"-adds ]; then
    echo "skipping $y-adds"
  else
    echo "creating $y-adds..."
    diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$y"-adds
  fi
  (( ++i ))
done
files=( *-sigs )
i=0 l=${#files[@]}
while (( i < l - 1 )); do
  j=$(( i + 1 ))
  x="${files[i]}" y="${files[j]}"
  if [ -e "$y"-rems ]; then
    echo "skipping $y-rems"
  else
    echo "creating $y-rems..."
    diff -Naur "$x" "$y" | grep ^- | cut -c2- | tail -n +2 > "$y"-rems
  fi
  if [ -e "$y"-adds ]; then
    echo "skipping $y-adds"
  else
    echo "creating $y-adds..."
    diff -Naur "$x" "$y" | grep ^+ | cut -c2- | tail -n +2 > "$y"-adds
  fi
  (( ++i ))
done
popd # reproducible
