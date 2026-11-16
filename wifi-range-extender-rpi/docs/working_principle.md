# Working Principle

## 1. Overview

The proposed Wi-Fi Range Extender uses a Raspberry Pi as an intermediate network device. It receives connectivity from an existing router through an upstream interface and provides a separate wireless access point for client devices.

The design uses two network interfaces:

- **Upstream interface (`wlan0` in the example):** connects to the existing router.
- **Access point interface (`wlan1` in the example):** broadcasts the extended Wi-Fi network.

Actual interface names depend on the hardware and operating system.

## 2. Main software components

### hostapd

`hostapd` manages the wireless access point. It defines the network name (SSID), wireless channel, operating mode, and WPA2-Personal security settings.

### dnsmasq

`dnsmasq` provides DHCP service to devices that join the extender network. In the example configuration, clients receive addresses from `192.168.4.2` through `192.168.4.20`, while the Raspberry Pi access point interface uses `192.168.4.1`.

### IP forwarding and NAT

IPv4 forwarding allows packets to move between the AP and upstream interfaces. Network Address Translation (NAT) rewrites outgoing client traffic so that it can use the upstream connection.

### Python monitoring

The monitoring script reads the station list from `hostapd_cli` and checks upstream wireless signal information using `iw`.

### Flask dashboard

The dashboard displays the connected-client list and upstream signal status in a browser. The `/api/status` endpoint returns the same basic status as JSON.

## 3. Data flow

1. A client device scans for available Wi-Fi networks.
2. The client connects to the SSID broadcast by the Raspberry Pi.
3. `hostapd` manages the wireless association and authentication.
4. `dnsmasq` assigns the client an IP address and network settings.
5. The client sends traffic through the Raspberry Pi.
6. IP forwarding and NAT pass permitted traffic to the upstream router.
7. Return traffic is forwarded back to the client.
8. The monitoring script and dashboard show basic network status.

## 4. Example network settings

| Setting | Example value |
|---|---|
| AP SSID | RPi_WiFi_Extender |
| AP interface | wlan1 |
| AP gateway | 192.168.4.1 |
| DHCP range | 192.168.4.2–192.168.4.20 |
| Subnet mask | 255.255.255.0 |
| Upstream interface | wlan0 |
| Wireless band | 2.4 GHz |

## 5. Security and deployment notes

- Replace the example passphrase with a unique strong password.
- Use WPA2-AES/CCMP rather than legacy TKIP.
- Do not expose the dashboard to untrusted networks.
- Confirm that the Wi-Fi adapter supports AP mode.
- Review firewall and forwarding rules before applying them.
- Configure persistent firewall rules using the mechanism supported by the installed OS.
- Newer Raspberry Pi OS releases may use NetworkManager rather than `dhcpcd`; adapt the network configuration accordingly.

## 6. Verification

A physical deployment should be verified by:
- Confirming that `hostapd` and `dnsmasq` are active.
- Connecting a phone or laptop to the extender SSID.
- Checking that the client receives an IP address.
- Pinging the extender gateway and upstream router.
- Testing internet access where permitted.
- Comparing signal strength and throughput at the same locations before and after deployment.

The included Packet Tracer screenshot is a separate simulation result and should not be confused with these physical deployment tests.
