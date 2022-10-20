# Setup Remote Development Environment

This repository contains a development environment for the Remote Development.

## Prerequisites
1. A Ubuntu machine on the cloud (e.g. AWS, GCP, Azure, DigitalOcean, Linode etc.)

## Setup
1. Download the following files from this repo (based on your requirement):
    - `setup.py` - It installs nvm, docker, php, composer and github cli
    - `setup-no-php.py` - It installs nvm, docker, and github cli
    
    Both of this script, ask you for `githubEmail` and `githubName` which are used to configure git. And also set default branch to `main` instead of `master`.


2. Now run the downloaded file using the following command:
```bash
python3 setup.py # or python3 setup-no-php.py
```

3. If you want to run the program from your browser, then install code-server using the script:
    - `codeserver.py` - It installs code-server in your cloud machine

4. Now run the downloaded file using the following command:
```bash
python3 codeserver.py
```

If you have created your remote machine on `Oracle` then you need to download and run the following file too.
```bash
python3 codeserver-postscript-in-oracle.py
```

5. Now you can access your remote machine from your browser using the following URL:
```bash
http://your-domain
```

> I have installed mine on `https://code.cb-ashik.co` and it's working fine.


## After the Setup
1. Install node using nvm
```bash
nvm install --lts (Installs the LTS version of node)
nvm install node (Installs the latest version of node)
```

2. Install yarn
```bash
npm install -g yarn
```


> Some of you might thought why I haven't installed databases in this setup. Well, I often setup databases using `docker-compose.yml` file. So, I don't need to install databases in my remote machine.
