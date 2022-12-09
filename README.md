# fdroid-misc-scripts

miscellaneous scripts to analyse f-droid app data

## Setup

```sh
$ git clone https://github.com/obfusk/fdroid-misc-scripts.git
$ cd fdroid-misc-scripts
$ git clone https://gitlab.com/fdroid/fdroiddata.git
```

## Scripts

### Index

#### download-index.sh

Downloads F-Droid's `index-v1.jar` & extracts `index-v1.json` from it.

```sh
$ ./scripts/download-index.sh
```

### Reproducible Builds: Binaries

#### download-binaries.sh

Downloads APKs for apps using `Binaries:` into `binaries/`.

```sh
$ ./scripts/download-binaries.sh
==> fdroiddata/metadata/some.app.id.yml
version=4.2 code=42
[...]

==> fdroiddata/metadata/some.other.app.id.yml
all versions disabled
[...]
```

#### compare-binaries.sh

Compares upstream and F-Droid APKs in `binaries/` (when both are available).

```sh
$ cd binaries
$ ../scripts/compare-binaries.sh cmp
some.app.id_42                                                          OK
some.other.app.id_37                                                    skipped
```

#### detect-signflinger.sh

Lists APKs in `binaries/` that are signed by Signflinger according to their
manifest, which is extracted using `apksigtool`.

```sh
$ cd binaries
$ ../scripts/compare-binaries.sh
```

NB: most -- but not all! -- of these APKs will start with a zipflinger virtual
entry (see next script).

#### detect-virtual-entry.sh

Lists APKs in `binaries/` whose first 28 bytes indicate they start with a
zipflinger virtual entry.

```sh
$ cd binaries
$ ../scripts/detect-virtual-entry.sh
```
