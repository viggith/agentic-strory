import argparse
import sys
from pathlib import Path


def list_directory(path: str = ".") -> list[str]:
    directory = Path(path)

    if not directory.exists():
        raise FileNotFoundError(f"Path does not exist: {directory}")

    if not directory.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {directory}")

    return sorted(entry.name for entry in directory.iterdir())


def main() -> int:
    parser = argparse.ArgumentParser(description="List the contents of a directory.")
    parser.add_argument("path", nargs="?", default=".", help="Directory to list")
    args = parser.parse_args()

    try:
        for entry in list_directory(args.path):
            print(entry)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(exc, file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
