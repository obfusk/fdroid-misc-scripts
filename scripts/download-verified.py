#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import os
import re
import subprocess
import time

URL = "https://verification.f-droid.org/{}"
VALID_APPID = re.compile(r"([a-zA-Z0-9_]+)(\.[a-zA-Z0-9_]+)*")


def download(output: str, url: str) -> None:
    args = ("wget", "-O", output, "--", url)
    subprocess.run(args, check=True)
    time.sleep(0.1)


def main() -> None:
    def save() -> None:
        print("saving verification/data.json...")
        with open("verification/data.json", "w") as fh:
            json.dump(data, fh, indent=2, sort_keys=True)
            fh.write("\n")
    os.makedirs("verification/tmp", exist_ok=True)
    veri_file = "verification/tmp/verified.json"
    if not os.path.exists(veri_file):
        download(veri_file, URL.format("verified.json"))
    with open(veri_file) as fh:
        veri_data = json.load(fh)
        apps = {appid: True for appid in veri_data["packages"]}
    with open("apps/metadata-apps") as fh:
        for line in fh:
            appid = line.strip()
            if appid not in apps:
                apps[appid] = False
    data = {}
    for i, (appid, from_json) in enumerate(sorted(apps.items())):
        print(f"[{i + 1}/{len(apps)}]")
        # if i and i % 100 == 0:
        #     save()
        verified_apks = set()
        unverified_apks = set()
        verified_since = {}
        if not VALID_APPID.fullmatch(appid):
            raise RuntimeError(f"Invalid appid: {appid!r}")
        app_file = f"verification/tmp/{appid}.json"
        if not os.path.exists(app_file):
            try:
                download(app_file, URL.format(appid + ".json"))
            except subprocess.CalledProcessError as e:
                if os.path.exists(app_file):
                    os.unlink(app_file)
                if from_json:
                    raise e
                else:
                    with open(app_file, "w") as fh:
                        json.dump({"404": True, "apkReports": []}, fh,
                                  indent=2, sort_keys=True)
                        fh.write("\n")
                    time.sleep(0.1)
                    continue
        with open(app_file) as fh:
            app_data = json.load(fh)
        if not app_data["apkReports"]:
            continue
        for report in app_data["apkReports"]:
            if not report.endswith(".apk.json") or not VALID_APPID.fullmatch(report[:-9]):
                raise RuntimeError(f"Invalid report: {report!r}")
            rep_file = f"verification/tmp/{report}"
            if not os.path.exists(rep_file):
                download(rep_file, URL.format(report))
            if not os.path.getsize(rep_file):
                print(f"WARNING: empty file: {rep_file!r}")
                continue
            with open(rep_file) as fh:
                rep_data = json.load(fh)
            assert rep_data
            apk = report[:-5]
            for ts, entry in sorted(rep_data.items(), reverse=True):
                if not entry["verified"]:
                    break
                verified_apks.add(apk)
                verified_since[apk] = time.strftime("%F", time.gmtime(float(ts)))
            if apk not in verified_apks:
                unverified_apks.add(apk)
        data[appid] = dict(
            verified_apks=sorted(verified_apks),
            unverified_apks=sorted(unverified_apks),
            verified_since=verified_since,
        )
    save()


if __name__ == "__main__":
    main()
