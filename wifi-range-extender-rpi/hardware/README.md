# 🔌 Hardware Documentation – Wi-Fi Range Extender using Raspberry Pi

## 1. Introduction

This folder contains the hardware requirements, component specifications, connection details, and hardware setup information for the Wi-Fi Range Extender using Raspberry Pi project.

The project uses a Raspberry Pi 4 Model B as the primary processing and networking unit.

An external USB Wi-Fi adapter is used to create an additional wireless access point, while the built-in wireless interface provides the upstream connection to an existing router.

The hardware setup is designed to be simple, modular, and suitable for educational networking experiments.

## 2. Hardware Components Required

The following hardware components are specified in the original project design.

| Sl. No. | Component | Specification | Quantity | Purpose |
|---|---|---|---:|---|
| 1 | Raspberry Pi | Raspberry Pi 4 Model B, 4 GB RAM | 1 | Main processing unit |
| 2 | MicroSD Card | 32 GB Class 10 / UHS-1 | 1 | Operating system and project storage |
| 3 | USB Wi-Fi Adapter | Alfa AWUS036NHA, Atheros AR9271 | 1 | Extended wireless access point |
| 4 | Power Supply | Official 5V/3A USB-C PSU | 1 | Power for Raspberry Pi |
| 5 | Ethernet Cable | Cat5e / Cat6 | 1 | Optional wired upstream connection |
| 6 | MicroSD Card Reader | USB 3.0 compatible | 1 | Operating system installation |
| 7 | HDMI Cable | Micro-HDMI to HDMI | 1 | Display connection |
| 8 | Monitor | HDMI-compatible | 1 | Initial configuration |
| 9 | Keyboard | Standard USB keyboard | 1 | User input |
| 10 | Mouse | Standard USB mouse | 1 | User interaction |
| 11 | LED | Standard LED | 1 | Optional status indication |
| 12 | Resistor | 330Ω | 1 | LED current limiting |

## 3. Detailed Hardware Description

### 3.1 Raspberry Pi 4 Model B

<text color="secondary" size="xs">Main processing and networking unit</text>

<AsyncImage query="Raspberry Pi 4 Model B 4GB board top view" aspectRatio="16:9" width="100%" maxHeight={190} fit="contain"/>

The Raspberry Pi 4 Model B is the main controller used in the project.

It is a single-board computer capable of running a Linux-based operating system and executing networking applications.

**Specifications:**

- Quad-core ARM Cortex-A72 processor.
- 4 GB RAM as specified in the project plan.
- Built-in 2.4 GHz and 5 GHz wireless networking capability.
- Gigabit Ethernet.
- USB 3.0 and USB 2.0 ports.
- GPIO interface.
- Micro-HDMI display output.
- USB-C power input.

**Purpose in the project:**

- Runs Raspberry Pi OS.
- Connects to the existing network.
- Controls the external Wi-Fi adapter.
- Runs hostapd and dnsmasq.
- Performs network forwarding and NAT.
- Executes Python monitoring scripts.
- Hosts the Flask dashboard.

### 3.2 MicroSD Card

<AsyncImage query="32GB SanDisk microSD card with SD adapter" aspectRatio="16:9" width="100%" maxHeight={150} fit="contain"/>

The MicroSD card stores the operating system and project files.

**Specification:**

- Capacity: 32 GB.
- Type: Class 10 / UHS-1.

**Purpose:**

- Stores Raspberry Pi OS.
- Stores network configuration files.
- Stores Python scripts.
- Stores monitoring information.
- Stores project documentation.

### 3.3 USB Wi-Fi Adapter

<AsyncImage query="Alfa AWUS036NHA USB WiFi adapter Atheros AR9271" aspectRatio="16:9" width="100%" maxHeight={170} fit="contain"/>

The USB Wi-Fi adapter provides the additional wireless interface required for the extended access point.

**Specification from the project plan:**

- Model: Alfa AWUS036NHA.
- Chipset: Atheros AR9271.
- Interface: USB.
- Wireless band: 2.4 GHz.
- AP mode: Supported with compatible driver configuration.

**Purpose:**

- Broadcasts the extended Wi-Fi SSID.
- Accepts smartphone and laptop connections.
- Operates through hostapd.
- Provides the wireless access point interface.

The adapter must be checked for driver compatibility and AP-mode support before deployment.

### 3.4 Power Supply

<AsyncImage query="Official Raspberry Pi 4 USB C 5V 3A power supply" aspectRatio="16:9" width="100%" maxHeight={150} fit="contain"/>

The power supply provides electrical power to the Raspberry Pi.

**Specification:**

- Output voltage: 5V.
- Current rating: 3A.
- Connector: USB-C.

**Purpose:**

- Powers the Raspberry Pi.
- Supports stable operation.
- Supplies power during networking and monitoring operations.

### 3.5 Ethernet Cable

<AsyncImage query="Cat6 Ethernet LAN cable RJ45" aspectRatio="16:9" width="100%" maxHeight={130} fit="contain"/>

An Ethernet cable is an optional component.

**Specification:**

- Category: Cat5e / Cat6.
- Connector: RJ45.

**Purpose:**

- Provides an alternative wired upstream connection.
- Connects the Raspberry Pi to the existing router.
- Can be used instead of the upstream Wi-Fi interface.

When Ethernet is used as the upstream connection, the forwarding and NAT configuration must use the correct Ethernet interface.

### 3.6 HDMI Cable and Monitor

<AsyncImage query="Raspberry Pi micro HDMI to HDMI cable computer monitor setup" aspectRatio="16:9" width="100%" maxHeight={150} fit="contain"/>

These components are used during initial Raspberry Pi configuration.

**Purpose:**

- Display the Raspberry Pi operating system.
- Access the desktop or terminal.
- Configure wireless networking.
- Troubleshoot system errors.

### 3.7 Keyboard and Mouse

<AsyncImage query="USB keyboard and mouse computer peripherals" aspectRatio="16:9" width="100%" maxHeight={130} fit="contain"/>

These are standard input devices used for local configuration.

**Purpose:**

- Enter terminal commands.
- Configure the operating system.
- Manage files.
- Execute project scripts.

### 3.8 LED and Resistor (Optional)

<AsyncImage query="LED 330 ohm resistor breadboard electronic components" aspectRatio="16:9" width="100%" maxHeight={140} fit="contain"/>

An optional LED circuit can be used as a basic hardware status indicator.

**Components:**

- One LED.
- One 330Ω resistor.
- Jumper wires.

**Purpose:**

- Provides a visual indication of GPIO-controlled activity.
- Demonstrates Raspberry Pi GPIO interfacing.
- Adds an optional hardware status indicator.

## 4. Hardware Connection Diagram

The proposed hardware connection arrangement is shown below.

```text
             Existing Wi-Fi Router
                      |
                      |
                Wireless Link
                      |
                      |
              Raspberry Pi 4
                      |
          +-----------+-----------+
          |           |           |
          |           |           |
       USB Port    USB-C Port   GPIO 17
          |           |           |
          |           |           |
     USB Wi-Fi    5V/3A PSU      LED
      Adapter                    |
       wlan1                   330Ω
                                  |
                                 GND

       Built-in Wi-Fi wlan0
                 |
                 |
          Existing Router
```

An alternative upstream connection can be established through Ethernet:

```text
Existing Router LAN
        |
        |
   Ethernet Cable
        |
        |
 Raspberry Pi eth0
        |
        |
 USB Wi-Fi Adapter wlan1
        |
        |
 Extended Wireless Network
```

## 5. GPIO Status LED Connection (Optional)

The project documentation includes an optional status LED connected to the Raspberry Pi.

**Connection details:**

| Component | Raspberry Pi Connection |
|---|---|
| LED Anode (+) | GPIO 17 (Physical Pin 11), through 330Ω resistor |
| LED Cathode (-) | GND (Physical Pin 6) |
| Resistor | 330Ω |

**Connection representation:**

```text
Raspberry Pi GPIO 17
          |
          |
       330Ω
       Resistor
          |
          |
       LED Anode (+)
          |
       LED Cathode (-)
          |
          |
     Raspberry Pi GND
```

The LED is optional and does not participate in wireless packet forwarding.

## 6. Hardware Assembly Procedure

### Step 1 – Prepare Raspberry Pi

Place the Raspberry Pi on a clean, non-conductive surface.

Ensure that the board is not exposed to moisture or conductive materials.

### Step 2 – Prepare MicroSD Card

Install Raspberry Pi OS onto the MicroSD card using Raspberry Pi Imager.

Insert the MicroSD card into the Raspberry Pi.

### Step 3 – Connect Display Peripherals

Connect the following components:

- Monitor through Micro-HDMI.
- Keyboard through USB.
- Mouse through USB.

These are required for local configuration but can be removed when using SSH.

### Step 4 – Connect Power Supply

Connect the official 5V/3A USB-C power supply to the Raspberry Pi.

Allow the operating system to boot.

### Step 5 – Connect USB Wi-Fi Adapter

Insert the compatible USB Wi-Fi adapter into an available USB port.

Verify that the adapter is detected by the operating system.

### Step 6 – Establish Upstream Connectivity

Connect the Raspberry Pi to the existing router using its built-in wireless interface or an optional Ethernet connection.

### Step 7 – Configure Access Point

Configure the external USB Wi-Fi adapter as the wireless access point through hostapd.

### Step 8 – Complete Network Configuration

Configure DHCP, IP forwarding, and NAT.

### Step 9 – Connect Wireless Clients

Connect a smartphone or laptop to the extended SSID.

### Step 10 – Verify Connectivity

Check the assigned IP address and test connectivity to the gateway and upstream router.

## 7. Hardware and Software Interaction

The hardware components work together with software services.

| Hardware Component | Related Software | Function |
|---|---|---|
| Raspberry Pi | Raspberry Pi OS | Main processing |
| Built-in Wi-Fi | Linux wireless networking | Upstream connection |
| USB Wi-Fi Adapter | hostapd | Wireless access point |
| Network Interfaces | iptables | Traffic forwarding and NAT |
| Raspberry Pi | dnsmasq | DHCP and DNS services |
| Raspberry Pi | Python | Monitoring |
| Raspberry Pi | Flask | Web dashboard |
| GPIO Pin 17 | GPIO library (if implemented) | Optional LED control |

## 8. Hardware Testing Checklist

The following checklist can be used during physical implementation.

- [ ] Raspberry Pi powers on successfully.
- [ ] Raspberry Pi OS boots correctly.
- [ ] MicroSD card is detected.
- [ ] USB Wi-Fi adapter is recognized.
- [ ] Adapter supports access point mode.
- [ ] Upstream network connection is established.
- [ ] Extended wireless network is broadcast.
- [ ] Smartphone detects the extended SSID.
- [ ] Smartphone connects using the configured password.
- [ ] DHCP assigns an IP address.
- [ ] Client can reach the extender gateway.
- [ ] Client can reach the upstream router.
- [ ] Internet connectivity works, where configured.
- [ ] Monitoring script displays connected clients.
- [ ] Flask dashboard displays network information.

## 9. Hardware Safety and Maintenance

The following precautions should be observed:

1. Use a suitable 5V/3A power supply.
2. Avoid connecting or disconnecting hardware while handling exposed circuitry.
3. Keep the Raspberry Pi in a ventilated environment.
4. Avoid short circuits on GPIO pins.
5. Use a current-limiting resistor with the optional LED.
6. Use compatible USB Wi-Fi adapters.
7. Keep the Raspberry Pi and USB adapter away from moisture.
8. Use secure wireless authentication.
9. Ensure that all connections are properly fitted.
10. Shut down the Raspberry Pi safely before removing its MicroSD card.

## 10. Circuit Simulation and PCB Design

The original project documentation proposes using TinkerCad or Fritzing to illustrate hardware connections.

The circuit design focuses on:

- Raspberry Pi power connection.
- USB peripheral connections.
- Ethernet connectivity.
- HDMI display connection.
- Optional GPIO status LED.

### Optional PCB Design

Since the project primarily uses a commercial Raspberry Pi single-board computer, a custom PCB is not mandatory.

An optional breakout or shield PCB may be designed for the status LED and expansion header.

Possible PCB design tools:

- KiCad 7.0.
- EasyEDA.
- Fritzing.

If a custom PCB is created, the following manufacturing files can be stored in the repository:

```text
hardware/
│
├── README.md
│
└── gerber/
    ├── top_copper.gbr
    ├── bottom_copper.gbr
    ├── top_silkscreen.gbr
    ├── board_outline.gbr
    ├── drill_file.drl
    └── gerber_archive.zip
```

These files should only be added if the PCB has actually been designed and exported.

## 11. Expected Hardware Outcome

After successful physical assembly and configuration, the hardware is expected to:

- Establish an upstream network connection.
- Broadcast an additional wireless network.
- Allow nearby client devices to connect.
- Support automatic IP address allocation.
- Forward permitted network traffic.
- Support connected-client monitoring.
- Provide a platform for wireless network testing.

The actual improvement in coverage depends on the installation environment, antenna performance, adapter capabilities, and upstream signal quality.

## 12. Conclusion

The hardware design of the Wi-Fi Range Extender uses a Raspberry Pi 4 Model B, MicroSD card, external USB Wi-Fi adapter, and suitable power supply to create an additional wireless access point.

The built-in wireless interface or optional Ethernet connection provides upstream connectivity, while the external adapter broadcasts the extended wireless network.

Optional peripherals such as the LED, HDMI monitor, keyboard, and mouse support hardware indication and initial configuration.

The modular hardware arrangement makes the project suitable for learning Raspberry Pi networking, wireless communication, Linux-based system configuration, and IoT networking concepts.
