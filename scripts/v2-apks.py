#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import glob
import json
import os
import sys
import yaml

# FIXME
show_missing = "--missing" in sys.argv[1:]
verbose = "--verbose" in sys.argv[1:] or "-v" in sys.argv[1:]

metadata_codes = {}
repo_codes = {}
archive_codes = {}

for file in glob.glob("fdroiddata/metadata/*.yml"):
    appid = os.path.splitext(os.path.basename(file))[0]
    with open(file) as fh:
        m = yaml.safe_load(fh.read())
    metadata_codes[appid] = sorted(
        b["versionCode"] for b in m["Builds"] if "disabled" not in b
    )

with open("v2/repo/index-v2.json") as fh:
    data = json.load(fh)
    for appid in sorted(data["packages"]):
        p = data["packages"][appid]
        repo_codes[appid] = sorted(
            x["manifest"]["versionCode"] for x in p["versions"].values()
        )

with open("v2/archive/index-v2.json") as fh:
    data = json.load(fh)
    for appid in sorted(data["packages"]):
        p = data["packages"][appid]
        archive_codes[appid] = sorted(
            x["manifest"]["versionCode"] for x in p["versions"].values()
        )

apps = set(metadata_codes) | set(repo_codes) | set(archive_codes)
for appid in sorted(apps):
    m = set(metadata_codes.get(appid, []))
    r = set(repo_codes.get(appid, []))
    a = set(archive_codes.get(appid, []))
    overlap = r & a
    if m != r | a or overlap:
        extra = (r | a) - m
        missing = m - (r | a)
        if extra or (show_missing and missing) or overlap:
            print(f"==> {appid}")
            if verbose:
                print(f"  metadata        : {', '.join(map(str, sorted(m)))}")
                print(f"  repo            : {', '.join(map(str, sorted(r)))}")
                print(f"  archive         : {', '.join(map(str, sorted(a)))}")
        if extra:
            if r - m:
                print(f"  extra (repo)    : {', '.join(map(str, sorted(r - m)))}")
            if a - m:
                print(f"  extra (archive) : {', '.join(map(str, sorted(a - m)))}")
        if show_missing and missing:
            print(f"  missing         : {', '.join(map(str, sorted(missing)))}")
        if overlap:
            print(f"  overlap (r & a) : {', '.join(map(str, sorted(overlap)))}")
