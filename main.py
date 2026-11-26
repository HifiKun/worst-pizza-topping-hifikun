#!/usr/bin/env python3
"""The Worst Pizza Topping.

Writes one funny line pitching the worst pizza topping imaginable to
/output/entry.txt for judging: a pizza topped with yesterday's cold
pizza slices, sold as if that were a feature.
"""

import os

ENTRY = (
    "Introducing the Leftover Pizza Pizza: yesterday's cold slices "
    "chopped up and baked onto fresh dough \u2014 d\u00e9j\u00e0 vu you can chew, "
    "because nothing says fresh like eating yesterday twice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
