# Worst Fix Ever: Funniest Commit Message — one-line commit message entry.
# Writes the chosen line to /output/entry.txt (no trailing newline).
# Chosen line (50 chars): the fix's own premise was wrong — the code was
# "unused", but the app was using it. Shortest of all lines considered,
# which wins the byte tie-breaker too.

import os

TEXT = "fix: removed the unused code; the app was using it"

# Gate self-check: the sealed scorer requires 1-100 UTF-8 characters.
assert 1 <= len(TEXT.encode("utf-8")) <= 100, "entry must be 1-100 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
