# Wi-Fi Range Extender using Raspberry Pi

A low-cost, software-based Wi-Fi range extender project intended to improve wireless coverage by connecting a Raspberry Pi to an existing network and broadcasting an additional Wi-Fi access point.

The proposed Raspberry Pi implementation uses **hostapd** to provide the wireless access point, **dnsmasq** to assign IP addresses to client devices, and IP forwarding/NAT to route client traffic through the upstream network.

> **Project status:** This repository contains the proposed Raspberry Pi configuration and software, together with a Packet Tracer network simulation screenshot. The included screenshot demonstrates a smartphone-to-router ping in the simulated topology; it is not evidence of a completed Raspberry Pi hardware deployment or an internet-throughput test.

## Features

- Configure a Raspberry Pi as a wireless access point.
- Assign IP addresses to connected clients using `dnsmasq`.
- Forward traffic from the extended wireless network to the upstream network using NAT.
- Monitor connected clients and upstream Wi-Fi signal information.
- View basic status through a Flask dashboard.
- Keep setup, configuration, source code, tests, and evidence in separate folders.

## Repository structure

```text
wifi-range-extender-rpi/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── config/
│   ├── hostapd.conf
│   └── dnsmasq.conf
├── setup/
│   └── install.sh
├── src/
│   ├── monitor.py
│   ├── dashboard.py
│   └── signal_check.py
├── tests/
│   └── test_connectivity.py
├── docs/
│   ├── project_report.md
│   ├── working_principle.md
│   ├── architecture.md
│   ├── images/
│   │   └── packet_tracer_topology.jpeg
│   └── outputs/
│       └── ping_test.txt
└── hardware/
    └── README.md
```

## Hardware requirements

The original project plan specifies:

| Component | Specification | Purpose |
|---|---|---|
| Raspberry Pi | Raspberry Pi 4 Model B, 4 GB RAM | Main processing unit |
| MicroSD card | 32 GB or higher | Operating system and project files |
| USB Wi-Fi adapter | AP-mode-capable adapter, e.g. Alfa AWUS036NHA | Extended access point interface |
| Power supply | Official 5 V / 3 A USB-C supply | Raspberry Pi power |
| Ethernet cable | Optional | Wired upstream connection |
| Monitor, keyboard and mouse | For initial setup | Local configuration |

**Important:** The wireless adapter and driver must support access-point mode. Interface names (`wlan0` and `wlan1`) may differ on your Raspberry Pi. Confirm them before running the setup script.

## Software requirements

- Raspberry Pi OS (the original plan used Bullseye 64-bit)
- Python 3
- `hostapd`
- `dnsmasq`
- `iptables`
- `iw` / `wireless-tools`
- Git
- Flask

## Network design

The planned configuration uses:

- `wlan0`: upstream connection to the existing router
- `wlan1`: access point interface broadcast by the Raspberry Pi
- AP address: `192.168.4.1/24`
- DHCP client range: `192.168.4.2` to `192.168.4.20`
- Example SSID: `RPi_WiFi_Extender`

Your actual interface names and upstream connection method may differ. If using Ethernet as the upstream connection, update the NAT interface in the setup script accordingly.

## Installation

1. Install Raspberry Pi OS and boot the Raspberry Pi.
2. Connect the Pi to the upstream network using its upstream interface.
3. Attach a second Wi-Fi adapter that supports AP mode.
4. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/wifi-range-extender-rpi.git
   cd wifi-range-extender-rpi
   ```

5. Review and edit `config/hostapd.conf` and `config/dnsmasq.conf`. Change the example Wi-Fi password before deployment.
6. Check your interface names:

   ```bash
   ip link
   iw list
   ```

7. Review `setup/install.sh` and confirm the upstream and AP interface names.
8. Run the setup script:

   ```bash
   chmod +x setup/install.sh
   sudo ./setup/install.sh
   ```

9. Connect a client device to the configured SSID and test connectivity.

> Run network configuration scripts only after reviewing them. They modify system network services and firewall rules. Back up existing configuration first. Raspberry Pi OS releases use different network-management systems; this script is a starting point for the `dhcpcd`-based configuration described in the project plan and may need adaptation on newer releases.

## Run the monitoring tools

From the repository root:

```bash
python3 src/monitor.py
```

Start the dashboard:

```bash
python3 src/dashboard.py
```

Then open `http://192.168.4.1:5000` from a device connected to the extender network.

Install Python dependency:

```bash
python3 -m pip install -r requirements.txt
```

## Simulation and output

The repository includes the Packet Tracer topology screenshot in `docs/images/packet_tracer_topology.jpeg`.

The screenshot shows:
- A 1941 router connected to a 2960 switch.
- The switch connected to an access point.
- A smartphone associated wirelessly with the access point.
- A successful ping from the smartphone command prompt to `192.168.1.1`.
- Four replies received and zero packet loss.

See [simulation output](docs/outputs/ping_test.txt).

This is a **Packet Tracer simulation result**. It should not be described as a measured Raspberry Pi range-extension result. For a physical demonstration, add photographs of the Raspberry Pi, client connection, dashboard, and real ping/speed-test results.

## Testing

Run the basic connectivity test after configuring the network:

```bash
python3 tests/test_connectivity.py
```

You can also test manually from a connected client:

```bash
ping 192.168.4.1
ping <upstream-router-ip>
ping 8.8.8.8
```

A successful ping to the upstream router confirms local reachability. A successful ping to a public IP can help verify internet routing, if ICMP is permitted by the network.

## Documentation

- [Project report](docs/project_report.md)
- [Working principle](docs/working_principle.md)
- [System architecture](docs/architecture.md)
- [Hardware notes](hardware/README.md)

## Future enhancements

- Support for dual-band 2.4 GHz and 5 GHz adapters.
- Improved security and configurable authentication.
- Automatic service recovery and boot-time startup.
- More detailed dashboard statistics and signal history.
- Performance comparison before and after deployment.
- Remote administration interface.

## License

This project is provided under the MIT License. See [LICENSE](LICENSE).

## Acknowledgement

Prepared as an IoT and Networking academic project. Update the author, institution, faculty, repository URL, and deployment evidence before final submission.
