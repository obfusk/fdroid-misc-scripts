#!/usr/bin/python3
# SPDX-FileCopyrightText: 2023 FC Stegerman <flx@obfusk.net>
# SPDX-License-Identifier: AGPL-3.0-or-later

import glob
import os

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
    return [os.path.basename(f)[:-5] for f in files], np.transpose(data)


def plot_data(title: str, dates: List[str], data: Any) -> None:
    labels = ["reproducible", "disabled", "missing"]
    colors = ["green", "red", "orange"]
    _, ax = plt.subplots()
    ax.stackplot(dates, np.vstack(data), labels=labels, colors=colors, alpha=0.8)
    ax.legend(loc="upper left")
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of apps")


def main() -> None:
    title_b = "Apps published with Reproducible Builds (Binaries)"
    dates_b, data_b = read_data(sorted(glob.glob("reproducible/*-bins")))
    plot_data(title_b, dates_b, data_b)
    plt.savefig("graphs/bins.png")

    title_s = "Apps published with Reproducible Builds (signatures in metadata)"
    dates_s, data_s = read_data(sorted(glob.glob("reproducible/*-sigs")))
    plot_data(title_s, dates_s, data_s)
    plt.savefig("graphs/sigs.png")

    assert dates_b == dates_s

    title_a = "Apps published with Reproducible Builds (all)"
    plot_data(title_a, dates_b, data_b + data_s)
    plt.savefig("graphs/rb.png")


if __name__ == "__main__":
    main()
