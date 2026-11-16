#!/usr/bin/env python3
"""Basic ping test for the extender gateway or another supplied host."""

import argparse
import platform
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Test network reachability with ping.")
    parser.add_argument("host", nargs="?", default="192.168.4.1",
                        help="Host/IP to ping (default: extender AP gateway)")
    args = parser.parse_args()

    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", count_flag, "4", args.host]

    try:
        result = subprocess.run(command, check=False, text=True)
    except OSError as exc:
        print(f"Could not run ping: {exc}")
        raise SystemExit(1)

    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
