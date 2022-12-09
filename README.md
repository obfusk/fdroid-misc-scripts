# fdroid-misc-scripts

miscellaneous scripts to analyse f-droid app data

## Setup

```sh
$ git clone https://github.com/obfusk/fdroid-misc-scripts.git
$ cd fdroid-misc-scripts
$ git clone https://gitlab.com/fdroid/fdroiddata.git
```

## Scripts

### Index & metadata

#### download-index.sh

Downloads F-Droid's `index-v1.jar` & extracts `index-v1.json` from it.

```sh
$ ./scripts/download-index.sh
```

#### update-index-and-metadata-apps.sh

Creates/updates `apps/index-apps`, `apps/metadata-apps`, etc.

```sh
$ ./scripts/update-index-and-metadata-apps.sh
getting apps from index-v1.json...
listing apps from metadata...
diffing...
$ ls -1 apps/
index-apps
index-apps-not-in-metadata
metadata-apps
metadata-apps-archived-and-disabled
metadata-apps-not-archived-or-disabled
metadata-apps-not-in-index
```

#### apps-status.py

Reads a list of appids from stdin and parses the metadata YAML for each app to
show its status: `disabled`, `archived`, `all builds disabled`, or `version=NAME
code=CODE` for the latest (non-disabled) build.

```sh
$ ./scripts/apps-status.py < apps/metadata-apps-not-in-index
some.app.id                                                   version=4.2 code=42
some.other.app.id                                             all builds disabled
[...]
```

### Reproducible Builds: Overview

#### update-rb.sh

Creates `reproducible/YYYY-MM-DD-{bins,sigs}`: an overview of the apps using
`Binaries`/`signatures` on that date.

NB: this doesn't *modify* `fdroiddata`, but it does check out the first commit
on the specified date (and then `master`).

```sh
$ ./scripts/update-rb.sh 2022-11-01
$ ./scripts/update-rb.sh 2022-12-01
```

<details>

```sh
$ cd reproducible
$ head 2022-12-01-bins
androdns.android.leetdreams.ch.androdns
ch.admin.bag.covidcertificate.verifier
ch.admin.bag.covidcertificate.wallet
com.dhaval.bookland
com.github.bmx666.appcachecleaner [signflinger]
com.markuspage.android.certtools [missing]
com.mishiranu.dashchan
com.rafapps.earthviewformuzei [signflinger]
com.zionhuang.music
de.corona.tracing
$ head 2022-12-01-sigs
de.schildbach.wallet
de.schildbach.wallet_test
dev.obfusk.jiten
dev.obfusk.jiten_webview
dev.obfusk.sokobang
org.schabi.newpipe [no longer RB]
org.torproject.torservices
```

</details>

To see what changed between two dates, you can use e.g.:

```sh
$ cd reproducible
$ diff -Naur 2022-{11,12}-01-bins | grep ^+ | cut -c2- | tail -n +2   # added
$ diff -Naur 2022-{11,12}-01-bins | grep ^- | cut -c2- | tail -n +2   # removed
```

#### update-rb-signflinger.sh

Updates `reproducible/signflinger` using `detect-virtual-entry.sh`.

```sh
$ ./scripts/update-rb-signflinger.sh
```

NB: `reproducible/{disabled,missing,no-longer-rb}` are updated manually.

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
[...]
```

#### detect-signflinger.sh

Lists APKs in `binaries/` that are signed by Signflinger according to their
manifest, which is extracted using `apksigtool`.

```sh
$ cd binaries
$ ../scripts/detect-signflinger.sh
some.app.id_42_fdroid.apk
some.app.id_42_upstream.apk
[...]
```

NB: most -- but not all! -- of these APKs will start with a zipflinger virtual
entry (see next script).

#### detect-virtual-entry.sh

Lists APKs in `binaries/` whose first 28 bytes indicate they start with a
zipflinger virtual entry.

```sh
$ cd binaries
$ ../scripts/detect-virtual-entry.sh
some.app.id_42_fdroid.apk
some.app.id_42_upstream.apk
[...]
```
