#!/usr/bin/env bash
# Initial setup helper for the Raspberry Pi Wi-Fi extender.
# Review interface names and OS networking configuration before running.

set -euo pipefail

UPSTREAM_IF="${UPSTREAM_IF:-wlan0}"
AP_IF="${AP_IF:-wlan1}"
AP_IP="192.168.4.1/24"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== Raspberry Pi Wi-Fi Range Extender setup ==="
echo "Upstream interface: ${UPSTREAM_IF}"
echo "Access point interface: ${AP_IF}"
echo
echo "Confirm these interfaces with: ip link"
read -r -p "Continue with package installation and network configuration? [y/N] " answer
if [[ "${answer}" != "y" && "${answer}" != "Y" ]]; then
    echo "Setup cancelled."
    exit 0
fi

sudo apt-get update
sudo apt-get install -y hostapd dnsmasq iptables iw wireless-tools python3 python3-pip

# This section is intended for dhcpcd-based Raspberry Pi OS installations.
if ! command -v dhcpcd >/dev/null 2>&1; then
    echo "dhcpcd was not found. Configure the AP interface using your OS network manager."
    echo "No dhcpcd configuration was written. Review the README before continuing."
    exit 1
fi

sudo systemctl stop hostapd || true
sudo systemctl stop dnsmasq || true

if ! grep -q "interface ${AP_IF}" /etc/dhcpcd.conf; then
    sudo tee -a /etc/dhcpcd.conf >/dev/null <<EOF

# Wi-Fi Range Extender AP interface
interface ${AP_IF}
static ip_address=${AP_IP}
nohook wpa_supplicant
EOF
fi

sudo install -m 0644 "${REPO_DIR}/config/hostapd.conf" /etc/hostapd/hostapd.conf
sudo install -m 0644 "${REPO_DIR}/config/dnsmasq.conf" /etc/dnsmasq.conf

# Enable IPv4 forwarding.
if grep -qE '^[# ]*net.ipv4.ip_forward=' /etc/sysctl.conf; then
    sudo sed -i 's/^[# ]*net.ipv4.ip_forward=.*/net.ipv4.ip_forward=1/' /etc/sysctl.conf
else
    echo 'net.ipv4.ip_forward=1' | sudo tee -a /etc/sysctl.conf >/dev/null
fi
sudo sysctl -w net.ipv4.ip_forward=1

# Configure NAT for traffic leaving through the upstream interface.
sudo iptables -t nat -C POSTROUTING -o "${UPSTREAM_IF}" -j MASQUERADE 2>/dev/null || \
    sudo iptables -t nat -A POSTROUTING -o "${UPSTREAM_IF}" -j MASQUERADE
sudo iptables -C FORWARD -i "${AP_IF}" -o "${UPSTREAM_IF}" -j ACCEPT 2>/dev/null || \
    sudo iptables -A FORWARD -i "${AP_IF}" -o "${UPSTREAM_IF}" -j ACCEPT
sudo iptables -C FORWARD -i "${UPSTREAM_IF}" -o "${AP_IF}" -m state --state RELATED,ESTABLISHED -j ACCEPT 2>/dev/null || \
    sudo iptables -A FORWARD -i "${UPSTREAM_IF}" -o "${AP_IF}" -m state --state RELATED,ESTABLISHED -j ACCEPT

sudo systemctl unmask hostapd || true
sudo systemctl enable hostapd dnsmasq
sudo systemctl restart dhcpcd
sudo systemctl restart dnsmasq
sudo systemctl restart hostapd

python3 -m pip install --user -r "${REPO_DIR}/requirements.txt"

echo
echo "Setup commands completed."
echo "Reboot if the AP interface does not come up automatically."
echo "Check services with: systemctl status hostapd dnsmasq"
