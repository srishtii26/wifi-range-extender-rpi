# Wi-Fi Range Extender using Raspberry Pi

## Aim

To design and deploy a Wi-Fi range extender using a Raspberry Pi to improve wireless coverage and reduce dead zones through a configurable, software-based access point.

## Problem statement

A single wireless router may not provide uniform coverage in homes, offices, and educational spaces. Walls, distance, interference, and building layout can weaken signals and create areas with poor connectivity. Commercial range extenders may also be costly or provide limited customization.

This project proposes a low-cost and configurable approach using a Raspberry Pi, wireless access point software, DHCP services, and network address translation.

## Proposed solution

The Raspberry Pi connects to an existing network through an upstream interface and broadcasts a separate wireless network through an AP-capable Wi-Fi interface. `hostapd` manages the access point, `dnsmasq` assigns IP addresses, and forwarding/NAT routes client traffic.

## Scope

### Included in the proposed design

- Configure the Raspberry Pi as a wireless access point.
- Provide DHCP addressing to wireless clients.
- Forward and translate client traffic to the upstream network.
- Configure SSID, password, and wireless channel.
- Monitor connected clients and upstream signal information.
- Provide a basic Flask status dashboard.

### Possible future enhancements

- Dual-band support where compatible hardware is available.
- Improved remote administration.
- Historical signal and client statistics.
- More extensive performance and coverage measurements.
- Additional authentication and network-management features.

## Hardware

- Raspberry Pi 4 Model B (4 GB RAM in the original plan).
- 32 GB MicroSD card.
- AP-mode-capable USB Wi-Fi adapter.
- Official 5 V / 3 A USB-C power supply.
- Optional Ethernet cable, monitor, keyboard, and mouse.

## Software

- Raspberry Pi OS.
- hostapd.
- dnsmasq.
- Python 3 and Flask.
- iptables.
- iw and Git.

## Simulation evidence

The supplied Packet Tracer screenshot shows a 1941 router, 2960 switch, access point, and smartphone. The smartphone successfully pings `192.168.1.1`; the displayed statistics show four packets sent, four received, and zero packet loss.

This is simulation evidence only. It does not establish that the Raspberry Pi hardware configuration has been deployed or that Wi-Fi coverage has increased.

## Expected outcome

After successful physical configuration, a client should be able to connect to the Raspberry Pi access point, receive an IP address from the DHCP service, and route permitted traffic through the upstream network. The dashboard should display connected clients and upstream signal information.

## Conclusion

The project provides an educational implementation plan for extending wireless connectivity with a Raspberry Pi and open-source networking tools. The repository separates configuration, setup scripts, monitoring code, documentation, and simulation evidence to make the project easier to understand, reproduce, and extend.
