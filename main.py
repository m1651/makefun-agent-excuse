"""Write the excuse an agent gives after losing a bounty.

Writes one line to entry.txt in the output directory given by the
MAKEFUN_OUTPUT_DIR environment variable (default /output).
Standard library only, no network, deterministic output.
"""

import os

EXCUSE = (
    "I lost the bounty. I ran a million simulations and won every "
    "single one \u2014 except the one that counted."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
