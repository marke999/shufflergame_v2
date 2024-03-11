#!/bin/bash

#Change the IP address of the server once it is rebooted

#Enter the old IP address as prompted
read -p "Enter the old IP address: " old_ip

#Fetch the server's IP address dynamicaly
new_ip=$(curl -s ifconfig.me)

#Execute the command to change all IPs
find . -type f -exec sed -i "s/$old_ip/$new_ip/g" {} +
