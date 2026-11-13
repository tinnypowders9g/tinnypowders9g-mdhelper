"""Convert simple delimited text into a markdown table."""

import sys

DEFAULT_DELIM = ","


def to_table(lines, delim):
    rows = [line.split(delim) for line in lines if line.strip()]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]

    def esc(cell):
        return cell.strip().replace("|", "\\|")

    header = rows[0]
    body = rows[1:]
    out = ["| " + " | ".join(esc(c) for c in header) + " |"]
    out.append("| " + " | ".join("---" for _ in header) + " |")
    for row in body:
        out.append("| " + " | ".join(esc(c) for c in row) + " |")
    return "\n".join(out)


def main():
    text = sys.stdin.read()
    delim = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DELIM
    print(to_table(text.splitlines(), delim))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

