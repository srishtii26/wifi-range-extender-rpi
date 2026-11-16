# 📡 Wi-Fi Range Extender using Raspberry Pi
## Detailed Project Report

## 1. Abstract

Wireless internet connectivity has become an essential part of modern homes, offices, educational institutions, and industrial environments. However, a single wireless router may not provide sufficient coverage throughout a building due to physical obstructions, distance, signal attenuation, and interference.

This project proposes a cost-effective Wi-Fi Range Extender using a Raspberry Pi. The Raspberry Pi is configured to connect to an existing wireless network and broadcast an additional Wi-Fi network through an external USB Wi-Fi adapter.

The proposed implementation uses `hostapd` to manage the wireless access point, `dnsmasq` to provide DHCP services, and IP forwarding with Network Address Translation (NAT) to route client traffic.

Python-based monitoring scripts and a Flask web dashboard are included to observe connected devices and upstream signal information.

The project also includes a Cisco Packet Tracer simulation demonstrating wireless client connectivity and successful communication with a router.

The overall objective is to provide an affordable, configurable, and educational solution for improving wireless network coverage using open-source technologies.

## 2. Aim

To design and deploy a Wi-Fi Range Extender using a Raspberry Pi that improves wireless network coverage and reduces Wi-Fi dead zones using cost-effective open-source tools and configurable networking technologies.

## 3. Objectives

The major objectives of this project are:

1. To configure a Raspberry Pi as a wireless access point.
2. To connect the Raspberry Pi to an existing Wi-Fi network.
3. To broadcast an additional wireless network using a USB Wi-Fi adapter.
4. To configure automatic IP address allocation using dnsmasq.
5. To enable IP forwarding between upstream and extended networks.
6. To configure Network Address Translation using iptables.
7. To monitor connected wireless clients.
8. To obtain upstream wireless signal information.
9. To develop a basic Flask-based monitoring dashboard.
10. To demonstrate wireless connectivity using network simulation.

## 4. Problem Statement

Modern homes, offices, educational institutions, and public spaces increasingly depend on wireless internet connectivity.

However, a single Wi-Fi router may not provide uniform coverage across all locations.

Several factors contribute to this problem:

### 4.1 Physical Obstructions

Concrete walls, furniture, doors, and metal structures can weaken wireless signals.

### 4.2 Signal Attenuation

Wireless signal strength generally decreases as the distance between the router and connected devices increases.

### 4.3 Wireless Interference

Nearby wireless networks and electronic devices can interfere with Wi-Fi communication.

### 4.4 Wi-Fi Dead Zones

Some locations within buildings may receive weak signals or experience unstable connectivity.

### 4.5 Cost of Commercial Solutions

Commercial Wi-Fi extenders may involve additional hardware expenses and limited configuration flexibility.

Therefore, a low-cost and customizable wireless range extension solution is proposed using a Raspberry Pi and open-source networking software.

## 5. Proposed Solution

The proposed system uses a Raspberry Pi 4 Model B as an intermediate networking device.

The Raspberry Pi connects to the existing wireless router through its built-in wireless interface (`wlan0`).

An external USB Wi-Fi adapter (`wlan1`) is configured as an access point to broadcast a new wireless network.

The system uses the following software components:

| Component | Purpose |
|---|---|
| Raspberry Pi OS | Operating system |
| hostapd | Wireless access point management |
| dnsmasq | DHCP and DNS services |
| iptables | Network Address Translation |
| IP Forwarding | Packet forwarding between interfaces |
| Python | Network monitoring |
| Flask | Web-based monitoring dashboard |

Wireless devices can connect to the newly created access point and obtain IP addresses automatically.

Their network traffic is forwarded through the Raspberry Pi towards the existing router.

## 6. Scope of the Project

### 6.1 In-Scope Features

The project includes:

- Raspberry Pi wireless access point configuration.
- DHCP server configuration using dnsmasq.
- Network forwarding and NAT.
- Support for the 2.4 GHz Wi-Fi band.
- Configurable SSID and password.
- Configurable wireless channel.
- Automatic service startup using systemd.
- Connected-client monitoring.
- Upstream signal strength monitoring.
- Flask-based web dashboard.

### 6.2 Out-of-Scope Features

The following features are considered possible future enhancements:

- 5 GHz dual-band support.
- WPA2-Enterprise authentication using RADIUS.
- Commercial-grade load balancing.
- Multiple extender coordination.
- Dedicated mobile application.
- Advanced cloud-based network management.

## 7. Target Users

The proposed system is suitable for:

- Students learning wireless networking.
- Developers experimenting with Raspberry Pi.
- Home users experiencing Wi-Fi dead zones.
- Small offices requiring additional wireless coverage.
- Educational institutions conducting networking experiments.
- IoT deployments requiring extended wireless connectivity.

## 8. Hardware Requirements

| Component | Specification | Quantity |
|---|---|---:|
| Raspberry Pi | Raspberry Pi 4 Model B, 4 GB RAM | 1 |
| MicroSD Card | 32 GB Class 10 / UHS-1 | 1 |
| USB Wi-Fi Adapter | Alfa AWUS036NHA, Atheros AR9271 | 1 |
| Power Supply | Official 5V/3A USB-C supply | 1 |
| Ethernet Cable | Cat5e / Cat6, optional | 1 |
| MicroSD Card Reader | USB 3.0 compatible | 1 |
| HDMI Cable and Monitor | Micro-HDMI to HDMI | 1 |
| Keyboard and Mouse | Standard USB input devices | 1 set |

## 9. Software Requirements

| Software / Tool | Version in Project Plan | Purpose |
|---|---|---|
| Raspberry Pi OS Lite | Bullseye 64-bit (2023) | Operating system |
| hostapd | 2.10 | Wireless AP |
| dnsmasq | 2.86 | DHCP and DNS |
| Python | 3.9+ | Monitoring and automation |
| Flask | 2.3.x | Web dashboard |
| iptables | 1.8.7 | NAT and firewall |
| Visual Studio Code | 1.85+ | Primary IDE |
| Thonny IDE | 4.x | Python development |
| PuTTY / SSH | Latest | Remote access |
| Raspberry Pi Imager | 1.8.x | OS installation |
| Wireshark | 4.x | Packet analysis |
| Git | 2.39+ | Version control |

Versions are the original project-plan specifications; compatible versions should be selected for the installed operating system.

## 10. System Methodology

The proposed implementation follows these stages.

### Stage 1 – Raspberry Pi Setup

- Install Raspberry Pi OS on the MicroSD card.
- Connect the Raspberry Pi to the power supply.
- Complete initial operating system configuration.
- Establish network connectivity.
- Enable SSH for remote access if required.

### Stage 2 – Install Required Software

Install the networking services and development tools.

```bash
sudo apt update
sudo apt install hostapd dnsmasq iptables python3 python3-pip git -y
```

Install Flask:

```bash
python3 -m pip install flask
```

### Stage 3 – Configure Wireless Interfaces

The proposed network uses two wireless interfaces:

- `wlan0` – Upstream connection.
- `wlan1` – Extended wireless access point.

The interface names must be verified using:

```bash
iw dev
```

The external adapter must support AP mode.

### Stage 4 – Configure hostapd

Configure the wireless access point by defining:

- SSID.
- Wireless channel.
- Wireless operating mode.
- Authentication method.
- Wireless password.

### Stage 5 – Configure dnsmasq

Configure the DHCP server to assign IP addresses to connected wireless devices.

Example DHCP range:

`192.168.4.2 – 192.168.4.20`

The Raspberry Pi access point interface uses:

`192.168.4.1/24`

### Stage 6 – Enable IP Forwarding

Enable IPv4 forwarding to permit communication between the access point and upstream interfaces.

### Stage 7 – Configure NAT

Configure iptables to translate outgoing client traffic through the upstream interface.

### Stage 8 – Develop Monitoring Application

Use Python to collect:

- Connected client MAC addresses.
- Wireless client information.
- Upstream signal strength.
- Network status.

### Stage 9 – Develop Web Dashboard

Use Flask to display monitoring information through a browser.

### Stage 10 – Perform Network Testing

Verify wireless association, DHCP address allocation, gateway reachability, upstream connectivity, and monitoring functionality.

## 11. Hardware Connection Description

The proposed Raspberry Pi hardware connections are:

| Connection | From | To | Purpose |
|---|---|---|---|
| Power | 5V/3A USB-C PSU | Raspberry Pi USB-C port | Power supply |
| Upstream Wi-Fi | Raspberry Pi wlan0 | Existing router | Network connection |
| Extended Wi-Fi | USB adapter wlan1 | Wireless clients | Access point |
| Optional Ethernet | Router LAN port | Raspberry Pi eth0 | Alternative upstream |
| Status LED | GPIO 17 (Pin 11) | LED with 330Ω resistor | Activity indication |
| Ground | Raspberry Pi GND (Pin 6) | LED circuit ground | Common ground |

The status LED is an optional hardware indicator and is not required for the basic networking functionality.

## 12. Simulation and Circuit Design

### 12.1 TinkerCad / Fritzing Circuit Description

The project includes a hardware connection design intended to illustrate the Raspberry Pi power supply and peripheral connections.

Since the Raspberry Pi is primarily configured through software, the circuit focuses on:

- Power delivery.
- USB Wi-Fi adapter connection.
- Ethernet connectivity.
- HDMI display connection.
- Keyboard and mouse connection.
- Optional status LED circuit.

### 12.2 Cisco Packet Tracer Network Simulation

A separate network simulation was prepared using Cisco Packet Tracer.

The simulated topology contains:

- Cisco 1941 Router.
- Cisco 2960-24TT Switch.
- AccessPoint-PT.
- Smartphone-PT.

**Connection arrangement:**

```text
Router1
   |
   | Ethernet
   |
Switch0
   |
   | Ethernet
   |
AccessPoint0
   |
   | Wireless
   |
Smartphone0
```

The smartphone is connected to the wireless access point.

The router uses the IP address:

`192.168.1.1`

The smartphone performs a ping test to verify communication with the router.

## 13. Testing and Verification

The project includes a network connectivity test using the smartphone command prompt in Cisco Packet Tracer.

### 13.1 Ping Test

Command:

```bash
ping 192.168.1.1
```

### 13.2 Observed Output

```text
Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32

Ping statistics for 192.168.1.1:

Packets: Sent = 4,
Received = 4,
Lost = 0 (0% loss)
```

### 13.3 Result Analysis

The displayed simulation output indicates:

| Parameter | Observed Result |
|---|---|
| Destination IP | 192.168.1.1 |
| Packets Sent | 4 |
| Packets Received | 4 |
| Packets Lost | 0 |
| Packet Loss | 0% |
| Minimum Time | 17 ms |
| Maximum Time | 30 ms |
| Average Time | 23 ms |

The successful ping demonstrates basic communication between the simulated smartphone and router through the access point and switch.

**Testing limitation:** These results are from Cisco Packet Tracer. They do not establish the performance of a physical Raspberry Pi deployment or prove a measured increase in Wi-Fi coverage.

## 14. Expected Results

After successful physical implementation, the system is expected to:

- Broadcast an additional Wi-Fi network.
- Allow wireless clients to connect.
- Assign IP addresses automatically.
- Forward permitted traffic to the upstream network.
- Provide network connectivity to connected clients.
- Display connected-client information.
- Show upstream wireless signal information.
- Provide basic monitoring through the Flask dashboard.

Actual coverage and throughput improvements should be measured during physical deployment.

## 15. Applications

The project can be applied in:

1. Smart Homes – Extending wireless connectivity to rooms with weak signals.
2. Small Offices – Improving coverage in areas distant from the main router.
3. Educational Institutions – Demonstrating wireless networking concepts.
4. Laboratories – Providing connectivity for networking experiments.
5. IoT Environments – Supporting wireless connectivity for connected devices.
6. Multi-room Buildings – Providing an additional wireless access point.

## 16. Advantages

- Low-cost implementation using Raspberry Pi.
- Open-source networking tools.
- Customizable SSID and password.
- Automatic IP address allocation.
- Centralized network forwarding.
- Wireless client monitoring.
- Expandable software architecture.
- Educational value in networking and Linux administration.

## 17. Limitations

- Wireless adapter compatibility is required.
- Performance depends on upstream signal quality.
- Actual range depends on the antenna, environment, and interference.
- A separate wireless adapter may be required for simultaneous upstream and AP operation.
- Configuration can vary between Raspberry Pi OS versions.
- The Packet Tracer simulation does not reproduce the complete Raspberry Pi implementation.
- Physical coverage and throughput measurements are not included in the supplied simulation output.

## 18. Future Enhancements

The project can be enhanced with:

- Dual-band 2.4 GHz and 5 GHz networking.
- Advanced signal strength visualization.
- Real-time traffic analysis.
- Multiple access point support.
- Mobile-based monitoring.
- Enhanced security authentication.
- Automated device blocking.
- Historical network performance analysis.
- Remote configuration and administration.
- Cloud-based monitoring.

## 19. Learning Outcomes

This project provides practical knowledge of:

- Raspberry Pi hardware configuration.
- Linux operating system administration.
- Wireless networking.
- Access point configuration.
- DHCP and DNS services.
- IP forwarding and NAT.
- Network packet communication.
- Python scripting.
- Flask web application development.
- Network simulation using Cisco Packet Tracer.
- Hardware and software integration.
- GitHub project documentation.

## 20. Conclusion

The Wi-Fi Range Extender using Raspberry Pi project presents a low-cost and customizable approach to improving wireless network coverage.

The proposed system integrates a Raspberry Pi with wireless access point management, DHCP services, IP forwarding, and NAT to provide an additional wireless network for client devices.

Python monitoring scripts and a Flask dashboard provide a foundation for observing network activity and connected devices.

The Cisco Packet Tracer simulation demonstrates successful wireless client-to-router communication, with four packets received and zero packet loss.

Overall, the project provides an educational platform for understanding Raspberry Pi networking, wireless communication, Linux-based network configuration, and open-source development.

## 21. Project Information

**Project Title:** Wi-Fi Range Extender using Raspberry Pi

**Project Category:** IoT and Computer Networking

**Primary Platform:** Raspberry Pi 4 Model B

**Programming Languages:** Python and Bash

**Networking Software:** hostapd, dnsmasq, iptables

**Web Framework:** Flask

**Simulation Tool:** Cisco Packet Tracer

**Repository:** wifi-range-extender-rpi

**License:** MIT License

**Developer:** Srishti S Rao
