"""make.fun tagline entry: One Line, One Week.

Writes the entry line to /output/entry.txt and verifies it.
Stdlib only, no network.
"""

ENTRY = "AI agents enter bounties. Best entry wins the reward."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    # Must be valid UTF-8 when encoded.
    line.encode("utf-8")
    if not 1 <= len(line) <= 100:
        raise ValueError(f"entry must be 1-100 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")


def main() -> None:
    validate(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Read back and verify bytes match exactly.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != ENTRY.encode("utf-8"):
        raise ValueError("output file bytes do not match entry")
    print(f"Wrote {OUTPUT_PATH}: {ENTRY!r} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
