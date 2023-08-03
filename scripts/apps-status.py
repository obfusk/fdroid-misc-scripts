#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
import sys
import yaml
for line in sys.stdin:
    appid = line.strip()
    with open(f"fdroiddata/metadata/{appid}.yml") as fh:
        m = yaml.safe_load(fh.read())
    if "Disabled" in m:
        msg = "disabled"
    elif "ArchivePolicy" in m and m["ArchivePolicy"] == 0:
        msg = "archived"
    else:
        for b in reversed(m["Builds"]):
            if "disable" not in b:
                name = b.get("versionName", "UNKNOWN")
                code = b["versionCode"]
                msg = f"version={name} code={code}"
                break
        else:
            msg = "all builds disabled"
    print(f"{appid:<61} {msg}")
