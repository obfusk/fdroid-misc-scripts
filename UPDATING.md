## Update fdroiddata & index

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
```

NB: scripts must be run in this order, after updating `binaries/`.

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
$ ../scripts/detect-signflinger.sh
$ ../scripts/detect-virtual-entry.sh
```
