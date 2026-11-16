# ⚙️ Working Principle – Wi-Fi Range Extender using Raspberry Pi

## 1. Introduction

The Wi-Fi Range Extender using Raspberry Pi works by receiving network connectivity from an existing wireless router and broadcasting a separate wireless network for nearby client devices.

The Raspberry Pi functions as an intermediate networking device between the existing router and wireless clients.

The system uses two network interfaces:

- **wlan0 – Upstream Interface:** Connects the Raspberry Pi to the existing Wi-Fi router.
- **wlan1 – Access Point Interface:** Broadcasts the extended wireless network through an external USB Wi-Fi adapter.

The complete process is managed using open-source networking services such as hostapd, dnsmasq, and iptables.

Python-based monitoring tools and a Flask dashboard are used to display information about connected devices and upstream signal strength.

## 2. Basic Working Concept

The proposed system operates through the following arrangement:

```text
       Existing Wi-Fi Router
                |
                |
          Internet / LAN
                |
                |
        Raspberry Pi 4
                |
        +-------+-------+
        |               |
      wlan0           wlan1
        |               |
   Upstream Wi-Fi   USB Wi-Fi Adapter
                        |
                     hostapd
                        |
                Extended Wi-Fi
                        |
                +-------+-------+
                |               |
            Smartphone        Laptop
```

The Raspberry Pi receives connectivity from the existing router through its upstream interface and provides an additional wireless access point through the external adapter.

## 3. Main Components and Their Working

### 3.1 Raspberry Pi 4 Model B

The Raspberry Pi acts as the main processing and networking unit.

It performs the following operations:

1. Establishes an upstream network connection.
2. Configures the external wireless adapter.
3. Runs the access point service.
4. Manages IP address allocation services.
5. Forwards network traffic.
6. Runs monitoring scripts.
7. Hosts the web dashboard.

The Raspberry Pi handles both wireless access point management and network traffic forwarding.

### 3.2 hostapd – Access Point Management

`hostapd` is a wireless access point daemon that allows the Raspberry Pi to broadcast a Wi-Fi network.

It manages the wireless access point configuration and client association.

Its functions include:

- Creating the Wi-Fi network.
- Broadcasting the configured SSID.
- Selecting the wireless channel.
- Configuring the operating mode.
- Enabling WPA2-Personal authentication.
- Managing connected wireless clients.

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

In this example:

- `interface=wlan1` selects the external Wi-Fi adapter.
- `ssid` specifies the network name.
- `hw_mode=g` selects the 2.4 GHz 802.11g mode.
- `channel=6` selects the wireless channel.
- `wpa=2` enables WPA2 security.
- `rsn_pairwise=CCMP` selects AES-based encryption.
- `wpa_passphrase` defines the wireless password.

### 3.3 dnsmasq – DHCP and DNS Service

`dnsmasq` provides DHCP and DNS forwarding services.

When a smartphone or laptop connects to the extended Wi-Fi network, it requires an IP address to communicate with other devices.

The DHCP server automatically assigns the required network configuration.

Example configuration:

```ini
interface=wlan1
bind-interfaces
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
server=8.8.8.8
server=8.8.4.4
```

The configuration provides:

- DHCP service on wlan1.
- Automatic IP address allocation.
- A subnet mask of 255.255.255.0.
- A DHCP lease duration of 24 hours.
- DNS forwarding to the configured DNS servers.

The Raspberry Pi access point interface is configured with:

`192.168.4.1/24`

Example IP allocation:

| Device | Example IP Address |
|---|---|
| Raspberry Pi AP interface | 192.168.4.1 |
| Smartphone | 192.168.4.2 |
| Laptop | 192.168.4.3 |
| Additional client | 192.168.4.4 |

The actual address assigned depends on DHCP availability.

### 3.4 IP Forwarding

IP forwarding allows the Raspberry Pi to transfer network packets between different network interfaces.

Without IP forwarding, the Raspberry Pi would not route client packets between the extended wireless network and upstream network.

Enable forwarding using:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

This enables IPv4 packet forwarding in the running system.

### 3.5 Network Address Translation (NAT)

NAT allows connected wireless devices to use the upstream network through the Raspberry Pi.

The client devices use private IP addresses from the extended network.

The Raspberry Pi translates outgoing traffic through its upstream interface.

Example:

```bash
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

The MASQUERADE rule changes the source address of outgoing packets to the address of the upstream interface.

This allows multiple connected devices to share the upstream network connection.

### 3.6 Python-Based Network Monitoring

The Python monitoring script observes the status of the wireless network.

It retrieves connected client information through `hostapd_cli`.

It also obtains upstream wireless signal information using wireless command-line utilities.

The monitoring system performs:

- Connected client identification.
- MAC address collection.
- Client count calculation.
- Signal strength retrieval.
- Periodic status updates.
- Terminal-based monitoring.

Example monitoring command:

```bash
python3 src/monitor.py
```

The monitoring interval in the original example is 10 seconds.

### 3.7 Flask Web Dashboard

Flask provides a browser-based interface for viewing the network status.

The dashboard retrieves information from the Python monitoring functions.

It displays:

- Upstream signal information.
- Number of connected clients.
- Connected client MAC addresses.
- Basic network status.

The dashboard also provides a JSON endpoint:

```text
/api/status
```

The web application can be started using:

```bash
python3 src/dashboard.py
```

The example dashboard address is:

```text
http://192.168.4.1:5000
```

## 4. Step-by-Step Working Process

### Step 1 – Existing Router Connection

The existing wireless router provides the original network connection.

The Raspberry Pi connects to this router using its upstream interface, `wlan0`.

### Step 2 – Raspberry Pi Network Initialization

The Raspberry Pi initializes its wireless interfaces.

The upstream interface connects to the existing network, while the external USB Wi-Fi adapter is configured for access point operation.

### Step 3 – Access Point Creation

The hostapd service starts and configures the wireless access point.

It broadcasts the configured SSID:

`RPi_WiFi_Extender`

Nearby wireless devices can discover this network.

### Step 4 – Wireless Authentication

A smartphone or laptop selects the extended network and enters the configured password.

The hostapd service manages the wireless association and WPA2-Personal authentication.

### Step 5 – IP Address Allocation

After connecting, the client requests an IP address using DHCP.

The dnsmasq service assigns an available address from the configured DHCP range.

For example:

`192.168.4.2`

The client also receives the relevant network settings.

### Step 6 – Client Network Communication

The connected device sends data packets through the Raspberry Pi access point interface.

The Raspberry Pi receives these packets through `wlan1`.

### Step 7 – Packet Forwarding

IP forwarding allows the Raspberry Pi to route the received packets towards the upstream interface.

### Step 8 – NAT Processing

The iptables NAT rule translates the outgoing client traffic.

The packets are then transmitted through the upstream interface towards the existing router.

### Step 9 – Return Traffic

The response packets return through the upstream network.

The Raspberry Pi uses its connection tracking and forwarding rules to direct the return traffic to the correct wireless client.

### Step 10 – Network Monitoring

The Python monitoring script collects information about connected wireless clients and upstream signal strength.

### Step 11 – Dashboard Display

The Flask application displays the collected network information through a web browser.

The dashboard provides a convenient way to observe the current network status.

## 5. Data Flow

The complete data flow can be represented as follows:

```text
Existing Wi-Fi Router
          |
          |
     wlan0 Interface
          |
          |
    Raspberry Pi
          |
          |
    wlan1 Interface
          |
          |
      hostapd
          |
          |
   Wireless Client
          |
          |
    DHCP Request
          |
          |
      dnsmasq
          |
          |
   Client IP Assigned
          |
          |
    Client Data Packet
          |
          |
     IP Forwarding
          |
          |
       NAT Rule
          |
          |
   Existing Router
          |
          |
   Destination Network
```

Monitoring runs alongside the networking process:

```text
hostapd_cli --------+
                    |
                    +---- Python Monitor
                    |          |
iw / wireless tools-+          |
                               |
                         Flask Dashboard
                               |
                           Web Browser
```

## 6. Example Network Configuration

| Network Parameter | Example Value |
|---|---|
| Existing Router | Upstream Wi-Fi router |
| Upstream Interface | wlan0 |
| Access Point Interface | wlan1 |
| Extended SSID | RPi_WiFi_Extender |
| Access Point Gateway | 192.168.4.1 |
| DHCP Start Address | 192.168.4.2 |
| DHCP End Address | 192.168.4.20 |
| Subnet Mask | 255.255.255.0 |
| Wireless Band | 2.4 GHz |
| Wireless Channel | 6 |
| Security | WPA2-Personal |

These values are example settings from the proposed configuration.

## 7. Network Connectivity Verification

After configuring the Raspberry Pi, the following tests should be performed.

### 7.1 Check Wireless Interfaces

```bash
iw dev
```

This command displays available wireless interfaces.

### 7.2 Check Access Point Service

```bash
sudo systemctl status hostapd
```

This checks whether the wireless access point service is active.

### 7.3 Check DHCP Service

```bash
sudo systemctl status dnsmasq
```

This checks whether the DHCP and DNS service is running.

### 7.4 Check Connected Clients

```bash
sudo hostapd_cli all_sta
```

This retrieves information about connected wireless stations.

### 7.5 Check Network Interfaces

```bash
ip addr
```

This displays configured IP addresses and interface information.

### 7.6 Check IP Forwarding

```bash
cat /proc/sys/net/ipv4/ip_forward
```

A value of `1` indicates that IPv4 forwarding is enabled.

### 7.7 Test Gateway Connectivity

From a connected smartphone or laptop:

```bash
ping 192.168.4.1
```

This tests communication with the Raspberry Pi access point gateway.

The upstream router and internet connectivity should also be tested separately.

## 8. Cisco Packet Tracer Simulation Working

A separate Cisco Packet Tracer simulation was prepared to demonstrate wireless connectivity.

The topology consists of:

- Cisco 1941 Router.
- Cisco 2960-24TT Switch.
- AccessPoint-PT.
- Smartphone-PT.

### Simulation Process

1. The router is connected to the switch through an Ethernet connection.
2. The switch is connected to the access point.
3. The smartphone connects wirelessly to the access point.
4. The smartphone opens its command prompt.
5. The command `ping 192.168.1.1` is executed.
6. The router responds to the ping requests.

### Observed Simulation Result

```text
Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32
Reply from 192.168.1.1: bytes=32

Packets: Sent = 4,
Received = 4,
Lost = 0 (0% loss)
```

The simulation demonstrates successful communication between the smartphone and router.

This result is from the Packet Tracer topology and is separate from physical Raspberry Pi testing.

## 9. Security Considerations

The following security practices should be followed:

- Use a strong and unique Wi-Fi password.
- Enable WPA2-Personal authentication.
- Use AES/CCMP encryption.
- Avoid exposing the dashboard to untrusted networks.
- Restrict access to administrative services.
- Review firewall and NAT rules.
- Keep the operating system and networking packages updated.
- Do not publish real Wi-Fi passwords or private network credentials in GitHub.

## 10. Important Deployment Considerations

1. Verify that the external Wi-Fi adapter supports AP mode.
2. Confirm the correct interface names before configuration.
3. Ensure that the upstream and extended networks use compatible but non-conflicting IP subnets.
4. Check whether the operating system uses NetworkManager or another network management service.
5. Configure persistent IP forwarding and firewall rules.
6. Ensure hostapd and dnsmasq do not conflict with other services.
7. Test connectivity before using the dashboard.
8. Measure signal strength and throughput at consistent locations to evaluate actual improvement.

## 11. Conclusion

The working principle of the Wi-Fi Range Extender is based on receiving network connectivity through one interface and providing an additional wireless access point through another interface.

The hostapd service manages wireless communication, dnsmasq provides automatic IP address allocation, and IP forwarding with NAT enables traffic movement between the extended and upstream networks.

Python monitoring and Flask provide a basic network monitoring interface.

This combination of Raspberry Pi hardware and open-source networking software provides a flexible educational implementation of a wireless range extension system.
