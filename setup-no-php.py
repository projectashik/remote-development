#!/usr/bin/env python3
import os

githubEmail = input("Enter your github email ")
githubName = input("Enter your github name ")

commands = [
    'sudo apt update',
    "sudo apt install build-essential -y",
    "git config --global user.email " + githubEmail,
    "git config --global user.name " + githubName,
    # NVM installation
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash",
     # Docker Setup
    'curl -fsSL https://get.docker.com  | sh',
    # Github Cli
    'curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg',
    'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null',
    'sudo apt update',
    'sudo apt install gh',
    # Docker Post Install Setup
    'sudo groupadd docker',
    'sudo usermod -aG docker $USER',
]

postScripts = [
'newgrp docker',
]

for cmd in commands:
  print("Running " + cmd)
  os.system(cmd)


print("Installed: nvm, docker, github cli")

for cmd in postScripts:
  os.system(cmd)
