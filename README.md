# 📡 Wi-Fi Range Extender using Raspberry Pi

A Raspberry Pi-based Wi-Fi Range Extender designed to improve wireless network coverage and reduce Wi-Fi dead zones using open-source networking technologies.

The project uses Raspberry Pi, wireless access point configuration, DHCP services, and network address translation (NAT) to extend network connectivity. It integrates `hostapd` for wireless access point management, `dnsmasq` for IP address allocation, and Python-based monitoring tools for observing connected devices and network signal information.

## 🚀 Overview

The **Wi-Fi Range Extender using Raspberry Pi** is designed to improve wireless connectivity in areas where the existing Wi-Fi router provides weak signals or limited coverage.

The Raspberry Pi acts as an intermediate networking device that connects to an existing wireless network and broadcasts an additional Wi-Fi network through a separate wireless interface.

The project demonstrates how a low-cost Raspberry Pi can be configured as a wireless repeater/access point using software-based networking technologies.

The platform combines:

- Raspberry Pi-based networking
- Wi-Fi Access Point configuration
- DHCP server using dnsmasq
- Wireless management using hostapd
- IP forwarding and Network Address Translation (NAT)
- Python-based network monitoring
- Flask-based monitoring dashboard
- Wireless connectivity testing

## 💡 Problem Statement

Wireless networks are widely used in homes, offices, educational institutions, and public spaces. However, a single Wi-Fi router may not provide uniform wireless coverage throughout a building.

Several factors contribute to poor Wi-Fi connectivity, including:

- Physical obstructions such as walls and furniture.
- Long distances between routers and client devices.
- Wireless signal interference.
- Weak signal strength in corners and different floors.
- Wi-Fi dead zones where connectivity becomes unreliable.

Commercial Wi-Fi range extenders can be expensive and may provide limited customization.

Therefore, a low-cost and customizable Wi-Fi range extension solution is required to improve wireless coverage using easily available hardware and open-source software.

## 🎯 Proposed Solution

The proposed system uses a Raspberry Pi as a Wi-Fi range extender to improve wireless network coverage.

The Raspberry Pi connects to an existing router through an upstream network interface and broadcasts an additional wireless network using a separate Wi-Fi adapter.

The system uses:

- **hostapd:** Configures the Raspberry Pi as a wireless access point.
- **dnsmasq:** Assigns IP addresses to connected wireless devices.
- **iptables:** Configures Network Address Translation (NAT).
- **IP Forwarding:** Allows network traffic to move between the upstream and extended networks.
- **Python:** Monitors connected devices and wireless signal information.
- **Flask:** Provides a web-based network monitoring dashboard.

This approach provides a configurable and cost-effective solution for extending wireless network connectivity.

## ✨ Features

### 📡 1. Wi-Fi Access Point Configuration

- Configure Raspberry Pi as a wireless access point.
- Create a separate Wi-Fi network.
- Configure SSID and password.
- Configure wireless channel settings.
- Support 2.4 GHz wireless networking with compatible hardware.

### 🌐 2. DHCP Server Configuration

The project uses `dnsmasq` to automatically assign IP addresses to devices connected to the extended Wi-Fi network.

Implemented functionality:

- Automatic IP address allocation.
- DHCP range configuration.
- Gateway configuration.
- DNS forwarding.
- Wireless client network management.

### 🔄 3. Network Address Translation (NAT)

Network Address Translation allows devices connected to the extended wireless network to communicate through the existing upstream network.

Implemented functionality:

- IPv4 forwarding.
- NAT configuration using iptables.
- Traffic forwarding between wireless interfaces.
- Upstream network connectivity.

### 🧠 4. Raspberry Pi Network Configuration

The Raspberry Pi acts as the central networking device.

Its responsibilities include:

- Connecting to the existing Wi-Fi network.
- Broadcasting the extended Wi-Fi network.
- Managing connected client devices.
- Forwarding network traffic.
- Providing wireless connectivity to client devices.

### 📊 5. Network Monitoring

Python-based monitoring scripts are included to observe the network status.

The monitoring functionality includes:

- Connected client identification.
- MAC address monitoring.
- Upstream Wi-Fi signal information.
- Periodic network status updates.
- Terminal-based monitoring.

### 🖥️ 6. Flask-Based Monitoring Dashboard

The project includes a Flask-based web dashboard for displaying basic network information.

The dashboard provides:

- Upstream Wi-Fi signal information.
- Connected client count.
- Connected device MAC addresses.
- Network status monitoring.
- JSON-based status endpoint.

### 🧪 7. Network Connectivity Testing

The project includes network connectivity testing to verify communication between connected devices and the router.

The Packet Tracer simulation demonstrates:

- Router-to-switch connectivity.
- Switch-to-access-point connectivity.
- Wireless smartphone association.
- Successful ping communication with the router.
- Zero packet loss in the displayed ping test.

## 🛠️ Tech Stack

### Hardware Components

- Raspberry Pi 4 Model B
- MicroSD Card (32 GB)
- USB Wi-Fi Adapter supporting AP mode
- 5V/3A USB-C Power Supply
- Ethernet Cable (Optional)
- HDMI Cable
- USB Keyboard and Mouse

### Programming Languages

- Python
- Bash Shell Scripting

### Networking Technologies

- Wi-Fi (IEEE 802.11)
- DHCP
- DNS
- IP Forwarding
- Network Address Translation (NAT)
- TCP/IP Networking

### Networking Software

- hostapd
- dnsmasq
- iptables
- iw
- wireless-tools

### Backend Development

- Python
- Flask

### Development Environment

- Raspberry Pi OS
- Visual Studio Code
- Thonny IDE
- PuTTY / SSH
- Git
- GitHub

### Simulation and Design Tools

- Cisco Packet Tracer
- Fritzing
- TinkerCad
- KiCad (Optional)

## 📁 Project Structure

```text
wifi-range-extender-rpi/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── config/
│   ├── hostapd.conf
│   └── dnsmasq.conf
│
├── setup/
│   └── install.sh
│
├── src/
│   ├── monitor.py
│   ├── dashboard.py
│   └── signal_check.py
│
├── docs/
│   ├── project_report.md
│   ├── working_principle.md
│   ├── architecture.md
│   │
│   ├── images/
│   │   └── packet_tracer_topology.jpeg
│   │
│   └── outputs/
│       └── ping_test.txt
│
├── tests/
│   └── test_connectivity.py
│
└── hardware/
    └── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/wifi-range-extender-rpi.git
```

### 2. Navigate to the Project Directory

```bash
cd wifi-range-extender-rpi
```

### 3. Update Raspberry Pi OS

```bash
sudo apt update
sudo apt upgrade -y
```

### 4. Install Required Packages

```bash
sudo apt install hostapd dnsmasq iptables iw wireless-tools python3 python3-pip git -y
```

### 5. Install Python Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 6. Configure the Wi-Fi Access Point

Edit the access point configuration:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Example configuration:

```ini
interface=wlan1
driver=nl80211
ssid=RPi_WiFi_Extender
hw_mode=g
channel=6
wpa=2
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
wpa_passphrase=ChangeThisPassword123
```

### 7. Configure the DHCP Server

Edit the dnsmasq configuration:

```bash
sudo nano /etc/dnsmasq.conf
```

Example configuration:

```ini
interface=wlan1
bind-interfaces
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
server=8.8.8.8
server=8.8.4.4
```

### 8. Configure IP Forwarding

Enable IPv4 forwarding:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

### 9. Configure Network Address Translation

For an upstream interface named `wlan0`:

```bash
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

### 10. Run the Setup Script

Review the interface names and configuration before executing:

```bash
chmod +x setup/install.sh
sudo ./setup/install.sh
```

### 11. Run the Network Monitoring Script

```bash
python3 src/monitor.py
```

### 12. Run the Flask Dashboard

```bash
python3 src/dashboard.py
```

Open the dashboard in a browser connected to the extended network:

```text
http://192.168.4.1:5000
```

**Important:** The above Raspberry Pi configuration is intended as a starting point for a `dhcpcd`-based Raspberry Pi OS setup. Interface names, network management, wireless adapter compatibility, and firewall persistence must be checked and configured for the actual device. The setup script should be reviewed before execution.

## 📊 System Workflow

The project follows the workflow below:

**Step 1 – Existing Wi-Fi Network**

The existing router provides the upstream internet or network connection.

**Step 2 – Raspberry Pi Connection**

The Raspberry Pi connects to the existing network using its upstream wireless interface (`wlan0`).

**Step 3 – Access Point Configuration**

The USB Wi-Fi adapter (`wlan1`) is configured as an access point using hostapd.

**Step 4 – DHCP Configuration**

The dnsmasq service automatically assigns IP addresses to devices connected to the extended Wi-Fi network.

**Step 5 – Network Traffic Forwarding**

IP forwarding and NAT allow connected devices to communicate through the upstream network.

**Step 6 – Client Connectivity**

Smartphones, laptops, and other wireless devices connect to the extended Wi-Fi network.

**Step 7 – Network Monitoring**

Python monitoring scripts and the Flask dashboard display connected devices and upstream signal information.

## 🖧 Network Topology

The project uses a network topology consisting of:

- Router
- Network Switch
- Wireless Access Point
- Smartphone / Wireless Client

The supplied Cisco Packet Tracer simulation demonstrates the connection between these network components.

### Simulation Screenshot

![Wi-Fi Range Extender Packet Tracer Topology](docs/images/packet_tracer_topology.jpeg)

The screenshot demonstrates a smartphone connected wirelessly to the access point through the simulated network.

## 📈 Simulation Output

The smartphone command prompt was used to test connectivity with the router.

**Command:**

```bash
ping 192.168.1.1
```

**Observed Results:**

```text
Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32

Ping statistics:
Packets: Sent = 4, Received = 4, Lost = 0
(0% loss)
```

**Result:**

The smartphone successfully communicated with the router at `192.168.1.1` through the simulated wireless topology.

> Note: This is the observed Cisco Packet Tracer simulation output. It should not be interpreted as a physical Raspberry Pi deployment or a measured Wi-Fi range improvement.

## 🔐 Security Considerations

The project demonstrates basic wireless network security through:

- WPA2 wireless authentication.
- Password-protected Wi-Fi access.
- Configurable SSID and channel.
- Controlled DHCP address allocation.
- NAT-based network forwarding.
- Network client monitoring.

A strong, unique Wi-Fi password should be configured before deployment. The monitoring dashboard should only be accessible to trusted network users.

## 📌 Future Improvements

The following features can be explored in future versions:

- Dual-band Wi-Fi support (2.4 GHz and 5 GHz).
- Improved wireless signal monitoring.
- Multiple access point support.
- Advanced network traffic monitoring.
- Real-time connected device notifications.
- Enhanced web-based administration.
- Automatic service recovery.
- Network performance comparison.
- Mobile-based monitoring application.
- Improved security and authentication mechanisms.

## 🎓 Learning Outcomes

Through this project, I developed practical knowledge of:

- Raspberry Pi configuration and Linux networking.
- Wireless networking and access point configuration.
- DHCP and DNS server configuration.
- Network Address Translation.
- IP forwarding and packet routing.
- Python-based network monitoring.
- Flask web application development.
- Cisco Packet Tracer network simulation.
- Hardware and software integration.
- Git and GitHub project management.

## 🌍 Real-World Applications

The proposed Wi-Fi range extender can be useful in:

- Smart Homes
- Small Offices
- Educational Institutions
- Laboratories
- Multi-room Buildings
- IoT Network Deployments
- Wireless Dead Zone Reduction

---
📬 Contact

Developer: Srishti S Rao

Degree: B.Tech – Electronics and Computer Engineering (AI/ML Specialization)

Institution: Christ University (Deemed to be University)

Location: Bengaluru, India

Email: srishtisrao26@gmail.com

LinkedIn: https://www.linkedin.com/in/srishti-s-rao-b09189316

GitHub: https://github.com/srishtii26
---

⭐ If you find this project interesting, consider giving the repository a star!

**Developed with a focus on Raspberry Pi, Wireless Networking, IoT, and Open-Source Technologies.**
