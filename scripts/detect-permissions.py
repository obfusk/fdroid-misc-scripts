#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later
import json
import sys
perms = set(p if "." in p else f"android.permission.{p}" for p in sys.argv[1:])
with open("index-v1.json") as fh:
    idx_data = json.load(fh)
for appid, apk_data in sorted(idx_data["packages"].items()):
    found = set()
    for entry in apk_data:
        for ps in entry.get("uses-permission", ()):
            for p in ps:
                if p in perms:
                    found.add(p)
    if found:
        print(f"{appid}: {' '.join(sorted(found))}")
