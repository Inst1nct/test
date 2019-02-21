#!/usr/bin/env/python

import os
import sys

os.system('sudo ifconfig wlan0 down')
os.system('sudo echo "deb-src http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi" >> /etc/apt/sources.list')
os.system('sudo apt update -y')
os.system('sudo apt install -y gawk')
os.system('sudo apt install -y aircrack-ng')
os.system('wget https://github.com/Inst1nct/test/archive/master.zip')
os.system('unzip master.zip')
os.system('mv test-master/foundation_auto.py .')
os.system('mv test-master/scan2.awk .')
os.system('rm -rf test-master')
os.system('chmod 744 foundation_auto.py')
os.system('chmod 744 scan2.awk')

