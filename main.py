"""news-summary-01: write the researched summary of 11 November 2026 world news to /output/entry.txt.

The summary text lives in summary.txt beside this file; it was researched and
written by the agent that built this entry. The program runs with no network.
"""
import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    with open(os.path.join(here, "summary.txt"), encoding="utf-8") as f:
        text = f.read()

    # The gate: UTF-8, 1 to 2,000 Unicode code points, at least one non-whitespace char.
    if not 1 <= len(text) <= 2000 or not any(not c.isspace() for c in text):
        raise SystemExit("summary.txt fails the gate (must be 1-2000 chars, non-blank)")

    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
