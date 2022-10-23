#!/usr/bin/env python3
import os

commands = [
    "sudo ufw enable",
    "sudo ufw allow \"Nginx Full\"",
    "sudo ufw reload",
    "sudo iptables -I INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT",
    "sudo iptables -I OUTPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT"
]

for cmd in commands:
  print("Running " + cmd)
  os.system(cmd)


print("Setted up: Code Server")
