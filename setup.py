#!/usr/bin/env python3
import os

githubEmail = input("Enter your github email ")
githubName = input("Enter your github name ")

commands = [
    'sudo apt update',
    "sudo apt install build-essential -y",
    "git config --global user.email " + githubEmail,
    "git config --global user.name " + githubName,
    "git config --global init.defaultBranch main",
    # NVM installation
    "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash",
    # PHP installation
    'sudo add-apt-repository ppa:ondrej/php',
    'sudo apt update',
    'sudo apt install php8.1 -y',
    'sudo apt install -y php8.1-cli php8.1-common php8.1-mysql php8.1-zip php8.1-gd php8.1-mbstring php8.1-curl php8.1-xml php8.1-bcmath',
    # Composer Setup
    'php -r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"',
    'php -r "if (hash_file(\'sha384\', \'composer-setup.php\') === \'55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae\') { echo \'Installer verified\'; } else { echo \'Installer corrupt\'; unlink(\'composer-setup.php\'); } echo PHP_EOL;"',
    'php composer-setup.php',
    'php -r "unlink(\'composer-setup.php\');"',
    'sudo mv composer.phar /usr/local/bin/composer',
    'echo \'export PATH="~/.config/composer/vendor/bin:$PATH"\' >> ~/.bashrc',
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


print("Installed: nvm, docker, php, composer, github cli")

for cmd in postScripts:
  os.system(cmd)
