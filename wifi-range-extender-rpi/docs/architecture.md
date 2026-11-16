# 🏗️ System Architecture – Wi-Fi Range Extender using Raspberry Pi

## 1. Introduction

The Wi-Fi Range Extender using Raspberry Pi is designed to improve wireless network coverage by using a Raspberry Pi as an intermediate networking device.

The system connects to an existing Wi-Fi router through an upstream network interface and broadcasts a separate wireless network through another Wi-Fi interface.

The architecture combines hardware components, wireless networking protocols, network configuration services, and Python-based monitoring tools.

The Raspberry Pi acts as the central processing and networking unit responsible for managing wireless clients and forwarding network traffic.

## 2. Overall System Architecture

The proposed architecture consists of the following major components:

1. Existing Wi-Fi Router
2. Raspberry Pi 4 Model B
3. Built-in Wireless Interface (wlan0)
4. USB Wi-Fi Adapter (wlan1)
5. Wireless Access Point Service (hostapd)
6. DHCP and DNS Service (dnsmasq)
7. IP Forwarding and NAT
8. Connected Client Devices
9. Python Monitoring System
10. Flask Web Dashboard

## 3. System Block Diagram

```text
                 EXISTING WI-FI ROUTER
                           |
                           |
                    Internet / LAN
                           |
                           |
              Raspberry Pi Upstream Interface
                       (wlan0)
                           |
                           |
                NETWORK PROCESSING UNIT
                    Raspberry Pi 4
                           |
             +-------------+-------------+
             |                           |
             |                           |
       IP Forwarding                 Python Monitor
             |                           |
             |                      Flask Dashboard
          NAT / iptables                  |
             |                       Web Browser
             |
       USB Wi-Fi Adapter
           (wlan1)
             |
             |
       hostapd Service
             |
             |
       Extended Wi-Fi Network
             |
       +-----+------+
       |            |
   Smartphone     Laptop
       |
   dnsmasq DHCP
   IP Allocation
```

**Note:** This diagram represents the proposed Raspberry Pi dual-interface implementation. DHCP operates on the extended client network, while the monitoring system observes network status.

## 4. Hardware Architecture

### 4.1 Raspberry Pi 4 Model B

The Raspberry Pi 4 Model B acts as the main processing and networking unit.

Responsibilities:

- Connect to the existing wireless router.
- Manage the extended Wi-Fi access point.
- Execute network configuration scripts.
- Forward network packets.
- Run Python monitoring applications.
- Host the Flask dashboard.

Specifications:

- Quad-core ARM Cortex-A72 processor.
- 4 GB RAM in the original project plan.
- Built-in wireless networking.
- Ethernet connectivity.
- USB ports for external peripherals.

### 4.2 Built-in Wi-Fi Interface (wlan0)

The built-in Wi-Fi interface is used as the upstream connection in the example design.

Responsibilities:

- Connect to the existing wireless router.
- Receive network connectivity.
- Provide the upstream route for connected clients.
- Supply upstream signal information for monitoring.

### 4.3 USB Wi-Fi Adapter (wlan1)

The external USB Wi-Fi adapter is configured as the extended wireless access point.

The original project plan specifies:

- Alfa AWUS036NHA.
- Atheros AR9271 chipset.
- Access Point mode support.

Responsibilities:

- Broadcast the extended SSID.
- Accept wireless client connections.
- Provide wireless connectivity.
- Operate through the hostapd service.

The adapter and driver must support AP mode. Actual interface names may differ depending on the operating system and connected hardware.

## 5. Software Architecture

The software architecture contains different services that work together to provide wireless connectivity.

### 5.1 hostapd – Wireless Access Point Management

`hostapd` is responsible for configuring and managing the wireless access point.

Functions:

- Configure the SSID.
- Configure wireless channel.
- Set wireless operating mode.
- Enable WPA2-Personal authentication.
- Manage wireless client associations.

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
wpa_passphrase=YOUR_STRONG_PASSWORD
```

### 5.2 dnsmasq – DHCP and DNS Management

`dnsmasq` provides DHCP and DNS forwarding services.

Functions:

- Assign IP addresses automatically.
- Provide gateway information.
- Configure DNS forwarding.
- Manage the extended wireless network.

Example configuration:

```ini
interface=wlan1
bind-interfaces
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
server=8.8.8.8
server=8.8.4.4
```

### 5.3 IP Forwarding

IP forwarding enables the Raspberry Pi to transfer packets between its upstream and access point interfaces.

It allows wireless client traffic to pass through the Raspberry Pi towards the existing router.

### 5.4 Network Address Translation (NAT)

NAT is configured using iptables.

It translates the source IP addresses of client traffic so that devices connected to the extended network can use the upstream network connection.

Example:

```bash
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

### 5.5 Python Monitoring System

The Python monitoring application collects information about connected devices and wireless signal status.

Functions:

- Retrieve connected client information.
- Read MAC addresses.
- Monitor upstream wireless signal strength.
- Display network status.
- Periodically update monitoring information.

The monitoring system uses `hostapd_cli` and wireless utilities such as `iw`.

### 5.6 Flask Web Dashboard

The Flask application provides a browser-based interface for displaying network information.

Dashboard features:

- Upstream signal information.
- Connected client count.
- Connected device MAC addresses.
- Network status.
- JSON-based status endpoint.

The application provides the following endpoints:

| Endpoint | Function |
|---|---|
| `/` | Displays the monitoring dashboard |
| `/api/status` | Returns network status in JSON format |

## 6. Network Interface Configuration

The proposed design uses two separate wireless interfaces.

| Parameter | Configuration |
|---|---|
| Upstream interface | wlan0 |
| Access point interface | wlan1 |
| Access point SSID | RPi_WiFi_Extender |
| Access point IP | 192.168.4.1 |
| Subnet mask | 255.255.255.0 |
| DHCP starting address | 192.168.4.2 |
| DHCP ending address | 192.168.4.20 |
| Wireless band | 2.4 GHz |
| Wireless channel | 6 |
| Security | WPA2-Personal |

These are example configuration values and should be adjusted according to the actual network environment.

## 7. Network Communication Flow

The network communication takes place in the following sequence:

1. The existing router provides upstream network connectivity.
2. Raspberry Pi connects to the router through wlan0.
3. The USB Wi-Fi adapter operates as an access point through wlan1.
4. hostapd broadcasts the configured SSID.
5. A smartphone or laptop discovers and connects to the extended Wi-Fi network.
6. dnsmasq assigns an IP address to the connected client.
7. The client sends network packets through the Raspberry Pi.
8. IP forwarding transfers packets between interfaces.
9. NAT translates the client traffic before sending it upstream.
10. Return traffic is forwarded to the connected wireless client.
11. Python monitoring collects network information.
12. Flask displays the collected information through the dashboard.

## 8. Network Topology Used in Cisco Packet Tracer

The supplied simulation screenshot contains the following components:

- Cisco 1941 Router.
- Cisco 2960-24TT Switch.
- AccessPoint-PT.
- Smartphone-PT.

### Physical Connections

| Source | Destination | Connection |
|---|---|---|
| Router1 | Switch0 | Ethernet |
| Switch0 | AccessPoint0 | Ethernet |
| AccessPoint0 | Smartphone0 | Wireless |

### Simulation Configuration

The smartphone is connected wirelessly to the access point.

The router is configured with the gateway address:

`192.168.1.1`

The smartphone performs a ping test to verify connectivity.

The displayed output confirms:

- Four packets transmitted.
- Four packets received.
- Zero packets lost.
- 0% packet loss.

**Important:** The Packet Tracer topology is a separate network simulation used to demonstrate wireless client-to-router connectivity. It is not a simulation of the Raspberry Pi's two-interface architecture.

## 9. System Architecture Advantages

- Low-cost networking solution.
- Open-source software implementation.
- Configurable wireless access point.
- Automatic client IP allocation.
- Centralized network management.
- Python-based monitoring.
- Expandable architecture.
- Suitable for educational networking experiments.

## 10. Future Architecture Enhancements

The architecture can be extended with:

- Dual-band wireless support.
- Multiple access points.
- Advanced traffic monitoring.
- Improved dashboard visualization.
- Remote network administration.
- Wireless client authentication enhancements.
- Historical signal strength analysis.
- Automated network recovery.

## 11. Conclusion

The proposed system architecture demonstrates how a Raspberry Pi can function as an intermediate wireless networking device.

By integrating hostapd, dnsmasq, IP forwarding, NAT, Python monitoring, and Flask, the system provides a modular and configurable approach to extending wireless network connectivity.

The architecture separates the upstream connection, access point functionality, traffic forwarding, and monitoring functions, making the project easier to maintain and enhance.
