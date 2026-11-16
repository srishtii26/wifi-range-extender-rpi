#!/usr/bin/env python3
"""Read connected station information and upstream Wi-Fi signal strength."""

import subprocess
import time
from datetime import datetime


def run_command(command):
    """Run a system command and return stdout, or an empty string on failure."""
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, check=False, timeout=8
        )
        return result.stdout.strip() if result.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def get_connected_clients():
    """Return MAC addresses reported by hostapd_cli."""
    output = run_command(["sudo", "hostapd_cli", "all_sta"])
    clients = []
    for line in output.splitlines():
        candidate = line.strip()
        parts = candidate.split(":")
        if len(parts) == 6 and all(len(part) == 2 for part in parts):
            try:
                int("".join(parts), 16)
                clients.append(candidate.upper())
            except ValueError:
                pass
    return clients


def get_signal_strength(interface="wlan0"):
    """Return signal information for the upstream wireless interface."""
    output = run_command(["iw", "dev", interface, "link"])
    if not output:
        return "Unavailable (check interface, connection, and iw permissions)"
    for line in output.splitlines():
        if "signal:" in line.lower():
            return line.strip()
    if "not connected" in output.lower():
        return "Not connected"
    return "Signal information unavailable"


def monitor_loop(interval=10):
    """Print connected clients and upstream signal at regular intervals."""
    print(f"Wi-Fi Extender Monitor | refresh interval: {interval}s")
    while True:
        clients = get_connected_clients()
        signal = get_signal_strength()
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        print(f"Connected clients: {len(clients)}")
        print(f"Upstream signal: {signal}")
        for client in clients:
            print(f" - {client}")
        time.sleep(interval)


if __name__ == "__main__":
    try:
        monitor_loop()
    except KeyboardInterrupt:
        print("\nMonitor stopped.")
