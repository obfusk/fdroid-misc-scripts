#!/bin/bash
firstofthismonth="$( date +%Y-%m-01 )"
date="${1:-$firstofthismonth}"
{
  echo "# All F-Droid apps published with Reproducible Builds ($date)"
  echo
  # shellcheck disable=SC2016
  cat reproducible/"$date"-{bins,sigs} | sort \
    | grep -Ev 'disabled|archived|missing' \
    | sed -r 's#^(\S+)#* [`\1`](https://f-droid.org/packages/\1)#'
} > reproducible/"$date"-all.md
