# Hardware and Circuit Files

The proposed project is primarily software-configured and uses a Raspberry Pi single-board computer with two network interfaces. No custom PCB is required for the core Wi-Fi extender functionality.

## Hardware connections

- Power the Raspberry Pi using a suitable USB-C power supply.
- Connect the upstream network through the built-in Wi-Fi interface or Ethernet.
- Connect an AP-mode-capable USB Wi-Fi adapter for the extended access point.
- Use a monitor, keyboard, and mouse for initial setup if required.

## Optional status LED

The original report describes an optional status LED connected to GPIO 17 (physical pin 11) through a 330-ohm resistor, with the other side connected to ground. The LED is not required for the network functionality and no LED-control program is included in this repository.

## Circuit / PCB evidence

Add your actual Fritzing, KiCad, or other circuit files here if you create them. Do not add placeholder Gerber files or claim that a PCB was fabricated if it was not.
