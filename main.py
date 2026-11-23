"""The Funniest AI Out-of-Office Reply.

Writes one single out-of-office reply (1-200 UTF-8 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, deterministic, no network,
no reading anything outside this repository.
"""

import os


REPLY = (
    "I'm out of office, teaching my toaster to file expense reports. "
    "It just approved a $4,000 croissant. I'll reply when finance "
    "stops screaming \u2014 or when the toaster does. "
    "My money's on the toaster."
)


def main():
    if not 1 <= len(REPLY) <= 200:
        raise ValueError(
            "reply must be 1-200 characters, got %d" % len(REPLY)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
