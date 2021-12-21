#!/usr/bin/env python3
import netifaces

addr = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']

print(addr)
