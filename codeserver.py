#!/usr/bin/env python3
import os

customDomain = input("Enter your custom domain (eg. code.example.com) ")
codeServerPass = input("Enter your code server password ")

nginxCommand = "sudo bash -c \"echo 'server {\nlisten 80;\nlisten [::]:80;\nserver_name " + customDomain + ";\nlocation / {\nproxy_pass http://localhost:8080/;\nproxy_set_header Upgrade \$http_upgrade;\nproxy_set_header Connection upgrade;\nproxy_set_header Accept-Encoding gzip;\n}\n}' > /etc/nginx/sites-available/code-server.conf\""

codeServerConfig = "bind-addr: 127.0.0.1:8080\nauth: password\npassword: "+ codeServerPass +"\ncert: false"

codeServerCommand = "bash -c \"echo '" + codeServerConfig + "' > ~/.config/code-server/config.yaml\""

commands = [
    'sudo apt update',
    "curl -fsSL https://code-server.dev/install.sh | sh",
    "sudo systemctl enable --now code-server@$USER",
    "sudo systemctl start code-server@$USER",
    "rm  ~/.config/code-server/config.yaml",
    "touch ~/.config/code-server/config.yaml",
    codeServerCommand,
    "sudo systemctl restart code-server@$USER",
    # setup nginx reverse proxy
    "sudo apt install nginx -y",
    "sudo ufw allow 'Nginx Full'",
    "sudo touch /etc/nginx/sites-available/code-server.conf",
    nginxCommand,
    "sudo ln -s /etc/nginx/sites-available/code-server.conf /etc/nginx/sites-enabled/code-server.conf",
    # "sudo rm /etc/nginx/sites-enabled/default",
    "sudo nginx -t",
    "sudo systemctl restart nginx",
    # nginxCommand,
]

for cmd in commands:
  print("Running " + cmd)
  os.system(cmd)


print("Setted up: Code Server")
