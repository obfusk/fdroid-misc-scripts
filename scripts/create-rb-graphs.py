#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import glob

from typing import Any, List, Tuple

import matplotlib.pyplot as plt     # type: ignore[import]
import numpy as np


def read_data(files: List[str]) -> Tuple[List[str], Any]:
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
    return [f[:-5] for f in files], np.transpose(data)


def plot_data(title: str, dates: List[str], data: Any) -> None:
    labels = ["reproducible", "disabled", "missing"]
    colors = ["green", "red", "orange"]
    _, ax = plt.subplots()
    ax.stackplot(dates, np.vstack(data), labels=labels, colors=colors, alpha=0.8)
    ax.legend(loc="upper left")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of apps")


def plot_and_save_bins() -> None:
    title = "Apps published with Reproducible Builds (Binaries)"
    dates, data = read_data(sorted(glob.glob("*-bins")))
    plot_data(title, dates, data)
    plt.savefig("bins.png")


def plot_and_save_sigs() -> None:
    title = "Apps published with Reproducible Builds (signatures in metadata)"
    dates, data = read_data(sorted(glob.glob("*-sigs")))
    plot_data(title, dates, data)
    plt.savefig("sigs.png")


if __name__ == "__main__":
    plot_and_save_bins()
    plot_and_save_sigs()
