## Update fdroiddata & v1 index

Manually: pull `fdroiddata`.

```sh
$ ./scripts/download-index.sh
$ ./scripts/update-index-and-metadata-apps.sh
```

NB: in this order.

## Update binaries

```sh
$ ./scripts/download-binaries.sh
```

Manually: inspect & clean up `binaries/`.

NB: after updating `fdroiddata`

## Update data & graphs for this month

```sh
$ FIRSTOFTHISMONTH="$( date +%Y-%m-01 )"
$ ./scripts/update-rb-signflinger.sh
$ ./scripts/update-rb.sh $FIRSTOFTHISMONTH
$ ./scripts/update-stats.sh $FIRSTOFTHISMONTH
$ ./scripts/update-diffs.sh
$ ./scripts/create-graphs.py
$ ./scripts/all-rb.sh
```

NB: scripts must be run in this order, after updating `binaries/`.

```sh
$ sed -r 's#^(\S+)#* [`\1`](https://f-droid.org/packages/\1)#' < reproducible/$FIRSTOFTHISMONTH-bins-adds
$ vim reproducible/overview.md
```

## Update verification server data

Manually: pull `f-droid.org-transparency-log`.

```sh
$ ./scripts/download-verified.py            # FIXME: cached
$ ./scripts/update-index-apks.sh 2023-01-   # FIXME: yearly
$ ./scripts/create-graphs.py
```

## Optional: check fdroiddata

```sh
$ ./scripts/apps-status.py < apps/index-apps-not-in-metadata
$ ./scripts/apps-status.py < apps/metadata-apps-not-in-index
$ ./scripts/detect-blocks-fdroiddata.sh
```

## Optional: check binaries

```sh
$ cd binaries
$ ../scripts/compare-binaries.sh cmp
$ ../scripts/detect-blocks.sh
```

## Optional: detect signflinger/virtual entry

```sh
$ cd binaries
$ ../scripts/detect-signflinger.sh
$ ../scripts/detect-virtual-entry.sh
```

## Optional: detect permissions

```sh
$ ./scripts/detect-permissions.py REQUEST_INSTALL_PACKAGES
```

## Optional: update v2 index

```sh
$ ./scripts/download-v2.sh
```

## Optional: detect v2 inconsistencies

NB: after updating `fdroiddata` and the v2 index.

```sh
$ ./scripts/v2-apks.py -v
```
