#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import glob
import json
import os

from typing import Any, List, Optional, Set, TextIO, Tuple

import matplotlib.pyplot as plt     # type: ignore[import]
import numpy as np


def read_rb_data(dates: List[str], what: str) -> Any:
    data = []
    for d in dates:
        repro = disabled = missing = 0
        with open(f"reproducible/{d}-{what}") as fh:
            for line in fh:
                line = line.rstrip()
                if " " in line:
                    tags = line.split(" ", 1)[-1][1:-1].split(", ")
                else:
                    tags = []
                if "disabled" in tags:
                    disabled += 1
                elif "missing" in tags:
                    missing += 1
                elif "no longer RB" not in tags:
                    repro += 1
        data.append([repro, disabled, missing])
    return np.transpose(data)


def read_apps_data(dates: List[str]) -> Any:
    data = []
    for d in dates:
        with open(f"stats/{d}-apps") as fh:
            total = set(line.rstrip() for line in fh)
        with open(f"reproducible/{d}-bins") as fh:
            repro = _rb_filter_apps(fh)
        with open(f"reproducible/{d}-sigs") as fh:
            repro |= _rb_filter_apps(fh)
        if not repro.issubset(total):
            print(f"WARNING: repro apps not in total on {d}:")
            for appid in sorted(repro - total):
                print(f"  {appid}")
        data.append([len(repro), len(total - repro)])
    return np.transpose(data)


def read_adds_data(dates: List[str]) -> Any:
    data = []
    for d in dates:
        with open(f"stats/{d}-adds") as fh:
            new_total = set(line.rstrip() for line in fh)
        with open(f"reproducible/{d}-bins-adds") as fh:
            new_repro = _rb_filter_apps(fh)
        with open(f"reproducible/{d}-sigs-adds") as fh:
            new_repro |= _rb_filter_apps(fh)
        if not new_repro.issubset(new_total):
            print(f"WARNING: new_repro apps not in new_total on {d}:")
            for appid in sorted(new_repro - new_total):
                print(f"  {appid}")
        data.append([len(new_repro), len(new_total - new_repro)])
    return np.transpose(data)


def read_rems_data(dates: List[str]) -> Any:
    data = []
    for d in dates:
        with open(f"stats/{d}-rems") as fh:
            new_total = set(line.rstrip() for line in fh)
        with open(f"reproducible/{d}-bins-rems") as fh:
            new_repro = _rb_filter_apps(fh)
        with open(f"reproducible/{d}-sigs-rems") as fh:
            new_repro |= _rb_filter_apps(fh)
        if not new_repro.issubset(new_total):
            print(f"WARNING: new_repro apps not in new_total on {d}:")
            for appid in sorted(new_repro - new_total):
                print(f"  {appid}")
        data.append([len(new_repro), len(new_total - new_repro)])
    return np.transpose(data)


def read_veri_apks_data() -> Tuple[Any, Any]:
    with open("verification/data.json") as fh:
        veri_data = json.load(fh)
    data = [_abs_to_pct([len(v["verified_apks"]), len(v["unverified_apks"])])
            for v in veri_data.values()]
    return np.arange(0, len(data)), np.transpose(data)


def read_veri_idx_data() -> Tuple[Any, Any]:
    data = []
    apks = {}
    with open("index-v1.json") as fh:
        idx_data = json.load(fh)
    with open("verification/data.json") as fh:
        veri_data = json.load(fh)
    for appid, apk_data in sorted(idx_data["packages"].items()):
        apks[appid] = sorted(set(x["apkName"] for x in apk_data))
    for appid, app_apks in apks.items():
        verified = unverified = untested = 0
        for apk in app_apks:
            if appid in veri_data:
                if apk in veri_data[appid]["verified_apks"]:
                    verified += 1
                elif apk in veri_data[appid]["unverified_apks"]:
                    unverified += 1
                else:
                    untested += 1
            else:
                untested += 1
        data.append(_abs_to_pct([verified, unverified, untested]))
    return np.arange(0, len(data)), np.transpose(data)


def read_veri_idx_t_data(dates: List[str]) -> Any:
    data = []
    with open("verification/data.json") as fh:
        veri_data = json.load(fh)
    for d in dates:
        verified = verified_later = unverified = untested = 0
        with open(f"verification/index-apks-{d}.json") as fh:
            idx_data = json.load(fh)
        for appid, app_apks in idx_data.items():
            for apk in app_apks:
                if appid in veri_data:
                    vs = veri_data[appid]["verified_since"]
                    if apk in vs:
                        if d >= vs[apk]:
                            verified += 1
                        else:
                            verified_later += 1
                    elif apk in veri_data[appid]["unverified_apks"]:
                        unverified += 1
                    else:
                        untested += 1
                else:
                    untested += 1
        data.append([verified, verified_later, unverified, untested])
    return np.transpose(data)


def _rb_filter_apps(fh: TextIO) -> Set[str]:
    skip = ("disabled", "missing", "no longer RB")
    apps = set()
    for line in fh:
        line = line.rstrip()
        if " " in line:
            appid, line = line.split(" ", 1)
            tags = line[1:-1].split(", ")
        else:
            appid = line
            tags = []
        if not any(t in tags for t in skip):
            apps.add(appid)
    return apps


def _abs_to_pct(values: List[int]) -> List[int]:
    tot = sum(values)
    return [round(100 * x / tot) for x in values]


def plot_rb_data(what: str, title: str, x: List[str], data: Any) -> None:
    labels = ["reproducible", "disabled", "missing"]
    colors = ["green", "red", "orange"]
    plot_data(what, title, x, data, colors=colors, labels=labels)


def plot_apps_data(what: str, title: str, x: List[str], data: Any, *,
                   ylabel: Optional[str] = None) -> None:
    labels = ["reproducible", "other"]
    colors = ["green", "blue"]
    plot_data(what, title, x, data, colors=colors, labels=labels, ylabel=ylabel)


def plot_veri_data(what: str, title: str, x: List[str], data: Any, *,
                   ylabel: Optional[str] = None) -> None:
    labels = ["verified", "unverified"]
    colors = ["green", "red"]
    if len(data) > 2:
        labels.append("untested")
        colors.append("orange")
    plot_data(what, title, x, data, figsize=(12.8, 4.8), colors=colors,
              labels=labels, xlabel=f"Apps (n={len(x)})", ylabel=ylabel, xticks=[])


def plot_veri_t_data(what: str, title: str, x: List[str], data: Any, *,
                     ylabel: Optional[str] = None) -> None:
    labels = ["verified at the time", "verified later", "unverified", "untested"]
    colors = ["green", "lime", "red", "orange"]
    plot_data(what, title, x, data, colors=colors, labels=labels, ylabel=ylabel)


def plot_data(what: str, title: str, x: List[str], data: Any, *,
              figsize: Tuple[float, float] = (6.4, 4.8),
              colors: List[str], labels: List[str], xlabel: Optional[str] = None,
              ylabel: Optional[str] = None, xticks: Optional[List[Any]] = None) -> None:
    _, ax = plt.subplots(figsize=figsize)
    ax.stackplot(x, np.vstack(data), labels=labels, colors=colors, alpha=0.8)
    ax.legend(loc="upper left")
    ax.set_title(title)
    ax.set_xlabel(xlabel or "Date")
    ax.set_ylabel(ylabel or "Number of apps")
    if xticks is not None:
        ax.set_xticks(xticks)
    print(f"saving graphs/{what}.png...")
    plt.savefig(f"graphs/{what}.png")


def create_graphs() -> None:
    dates = [os.path.basename(f)[:-5] for f in sorted(glob.glob("reproducible/*-bins"))]

    title_bins = "Apps published with Reproducible Builds (Binaries)"
    data_bins = read_rb_data(dates, "bins")
    plot_rb_data("bins", title_bins, dates, data_bins)

    title_sigs = "Apps published with Reproducible Builds (signatures in metadata)"
    data_sigs = read_rb_data(dates, "sigs")
    plot_rb_data("sigs", title_sigs, dates, data_sigs)

    title_all = "Apps published with Reproducible Builds (all)"
    plot_rb_data("rb", title_all, dates, data_bins + data_sigs)

    title_apps = "F-Droid apps (not 100% accurate)"
    data_apps = read_apps_data(dates)
    plot_apps_data("apps", title_apps, dates, data_apps)

    title_adds = "New apps (not 100% accurate)"
    data_adds = read_adds_data(dates[1:])
    plot_apps_data("adds", title_adds, dates[1:], data_adds, ylabel="Number of new apps")

    title_rems = "Removed apps (not 100% accurate)"
    data_rems = read_rems_data(dates[1:])
    plot_apps_data("rems", title_rems, dates[1:], data_rems, ylabel="Number of removed apps")

    title_veri_apks = "APKs verified by the Verification Server"
    x_veri_apks, data_veri_apks = read_veri_apks_data()
    plot_veri_data("veri_apks", title_veri_apks, x_veri_apks, data_veri_apks,
                   ylabel="% of tested APKs")

    title_veri_idx = "Verified APKs in the index"
    x_veri_idx, data_veri_idx = read_veri_idx_data()
    plot_veri_data("veri_idx", title_veri_idx, x_veri_idx, data_veri_idx,
                   ylabel="% of APKs in the index")

    idx_dates = [os.path.basename(f)[11:-5] for f in
                 sorted(glob.glob("verification/index-apks-*.json"))]

    title_veri_idx_t = "Verified APKs in the index over time (not 100% accurate)"
    data_veri_idx_t = read_veri_idx_t_data(idx_dates)
    plot_veri_t_data("veri_idx_t", title_veri_idx_t, idx_dates, data_veri_idx_t,
                     ylabel="Number of APKs in the index")


if __name__ == "__main__":
    create_graphs()
