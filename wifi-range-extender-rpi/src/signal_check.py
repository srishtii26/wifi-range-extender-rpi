#!/usr/bin/env python3
"""Display link and signal information for a selected Wi-Fi interface."""

import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Check Wi-Fi link signal.")
    parser.add_argument("--interface", default="wlan0", help="Wi-Fi interface name")
    args = parser.parse_args()

    try:
        result = subprocess.run(
            ["iw", "dev", args.interface, "link"],
            capture_output=True, text=True, check=False, timeout=8
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"Unable to run iw: {exc}")
        raise SystemExit(1)

    if result.returncode != 0:
        print(result.stderr.strip() or "Could not read Wi-Fi link.")
        raise SystemExit(result.returncode)

    print(result.stdout.strip() or "No link information returned.")


if __name__ == "__main__":
    main()
