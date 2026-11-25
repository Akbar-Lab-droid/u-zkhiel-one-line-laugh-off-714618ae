"""Entry program for the make.fun "One-Line Laugh-Off" bounty.

Reads the committed entry.txt (exactly one funny line that lands on a cold
read) and writes it to the harness output directory (MAKEFUN_OUTPUT_DIR,
default "out").
"""

import os
import shutil

# The entry is exactly one funny line, kept within the bounty limit.
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"),
                    os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
