#!/bin/bash

# configure_wifi.sh

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

# Check if environment variables are set
if [ -z "$WIFI_SSID" ] || [ -z "$WIFI_PASSWORD" ]; then
  echo "Error: WIFI_SSID or WIFI_PASSWORD environment variable is not set"
  exit 1
fi

# Create the wpa_supplicant.conf file
cat << EOF > /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="$WIFI_SSID"
    psk="$WIFI_PASSWORD"
}
EOF

echo "Wi-Fi configuration has been updated."

# Restart the wireless interface
wpa_cli -i wlan0 reconfigure

echo "Wireless interface has been reconfigured."