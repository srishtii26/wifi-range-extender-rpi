# System Architecture

## Block diagram

```text
                  Existing Wi-Fi Router
                          |
                    Upstream network
                          |
                  Raspberry Pi wlan0
                          |
                 IP forwarding + NAT
                          |
                  Raspberry Pi wlan1
                          |
                    hostapd (AP)
                          |
                 Extended Wi-Fi network
                    /           \
               Smartphone      Laptop
                          |
                    dnsmasq DHCP

        Python monitor + Flask dashboard
        observe clients and upstream signal
```

## Interface responsibilities

| Interface/service | Responsibility |
|---|---|
| `wlan0` | Upstream Wi-Fi connection in the example design |
| `wlan1` | Extended wireless access point |
| `hostapd` | Wireless access point management |
| `dnsmasq` | DHCP and DNS forwarding |
| IP forwarding | Allows traffic to pass between interfaces |
| NAT/iptables | Translates client traffic to the upstream interface |
| Python monitor | Reads connected-client and signal information |
| Flask | Displays status through a web page and JSON endpoint |

## Packet Tracer evidence

The provided screenshot depicts a separate simulated topology with a router, switch, access point, and smartphone. The phone successfully pings `192.168.1.1`. It demonstrates basic simulated wireless-to-router reachability, not the Raspberry Pi dual-interface architecture above.
