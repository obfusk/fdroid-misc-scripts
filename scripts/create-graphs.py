#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import glob
import os

from typing import Any, List

import matplotlib.pyplot as plt     # type: ignore[import]
import numpy as np


def read_rb_data(files: List[str]) -> Any:
    data = []
    for f in files:
        repro = disabled = missing = 0
        with open(f) as fh:
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
                elif "no longer RB" in tags:
                    pass
                else:
                    repro += 1
        data.append([repro, disabled, missing])
    return np.transpose(data)


def read_adds_data(dates: List[str]) -> Any:
    data = []
    for d in dates:
        with open(f"stats/{d}-adds") as fh:
            new_total = set(line.rstrip() for line in fh)
        with open(f"reproducible/{d}-bins-adds") as fh:
            new_repro = set(line.split()[0] for line in fh)
        with open(f"reproducible/{d}-sigs-adds") as fh:
            new_repro |= set(line.split()[0] for line in fh)
        if not new_repro.issubset(new_total):
            print(f"WARNING: new_repro apps not in new_total on {d}:")
            for appid in sorted(new_repro - new_total):
                print(f"  {appid}")
        data.append([len(new_total - new_repro), len(new_repro)])
    return np.transpose(data)


def plot_rb_data(title: str, dates: List[str], data: Any) -> None:
    labels = ["reproducible", "disabled", "missing"]
    colors = ["green", "red", "orange"]
    _, ax = plt.subplots()
    ax.stackplot(dates, np.vstack(data), labels=labels, colors=colors, alpha=0.8)
    ax.legend(loc="upper left")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of apps")


def plot_adds_data(title: str, dates: List[str], data: Any) -> None:
    labels = ["other", "reproducible"]
    colors = ["blue", "green"]
    _, ax = plt.subplots()
    ax.stackplot(dates, np.vstack(data), labels=labels, colors=colors, alpha=0.8)
    ax.legend(loc="upper left")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of new apps")


def create_graphs() -> None:
    dates = [os.path.basename(f)[:-5] for f in sorted(glob.glob("reproducible/*-bins"))]

    title_bins = "Apps published with Reproducible Builds (Binaries)"
    data_bins = read_rb_data(sorted(glob.glob("reproducible/*-bins")))
    plot_rb_data(title_bins, dates, data_bins)
    plt.savefig("graphs/bins.png")

    title_sigs = "Apps published with Reproducible Builds (signatures in metadata)"
    data_sigs = read_rb_data(sorted(glob.glob("reproducible/*-sigs")))
    plot_rb_data(title_sigs, dates, data_sigs)
    plt.savefig("graphs/sigs.png")

    title_all = "Apps published with Reproducible Builds (all)"
    plot_rb_data(title_all, dates, data_bins + data_sigs)
    plt.savefig("graphs/rb.png")

    title_adds = "New apps (not 100% accurate)"
    data_adds = read_adds_data(dates[1:])
    plot_adds_data(title_adds, dates[1:], data_adds)
    plt.savefig("graphs/adds.png")


if __name__ == "__main__":
    create_graphs()
