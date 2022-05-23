# Web Spider

To run this spider, use Ubuntu command line, install following with either env or install individually, run webspider behind VPN. Run test first to see if installed correctly, then run webspider.

# run test

    python3 test.py

# Run Webspider

    python3 webspider.py

# install

Ubuntu 20.02

Python 3

Pip

VirtualEnv

## Install Pip3

    sudo apt-get install python3-pip

## Install VirtualEnv

    python3 -m pip install --user virtualenv

## Install ensurepip

    sudo apt-get install python3-venv

## Create Virtual Env

    python3 -m venv env

## Activate virtual Env

    source env/bin/activate

## Install bs4

    python3 -m pip install bs4

## Install requests

    python3 -m pip install requests

## deactivate Virtual Env

    env/bin/deactivate

## Freeze and create requirements

    pip freeze > requirements.txt