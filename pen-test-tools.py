#!/usr/bin/python3

# Script Name: Pen Testing Tools
# Class Name: Ops 401
# Author Name: Carsten Rossen
# Date of Latest Revision: 6/8/21
# Purpose: Runs tedious pen testing tasks such as host enumeration, 
# comprehensive Nmap scans, and brute force attacks.


# Import libraries
import os 


# Declare functions

# Provide user with an option menu
def menu():
    print("Pick from these options:")
    print("1. Host enumeration")
    print("2. Comprehensive host scan")
    print("3. Brute force attack")
    choice = input("What would you like to do? ")
    return choice

# Get network to enumerate hosts on
def enumeration():
    network = input("\nNetwork to scan (ex: 10.0.0.0/24): ")
    command = "nmap -sn"
    run_command(command, network)

# Run the Nmap scan 
def run_command(command, target):
    # Give the user the option to save output to a text file
    make_file = input("Output to text file (y/n)? ")
    if make_file == 'y':
        filepath = input("File path for text file: ")
        os.system(f"{command} {target} > {filepath}")
    else:
        os.system(f"{command} {target}")

# Get host to run a comprehensive Nmap scan on
def scan_host():
    host = input("\nHost to scan (ex: 10.0.0.5): ")
    command = "nmap -sV -sC"
    run_command(command, host)

# Get host, protocol, and username to run a brute force attack on
def brute_force():
    host = input("\nHost to attack: ")
    protocol = input("Protocol (ex: rdp): ")
    username = input("Username: ")
    os.system(f"hydra -V -f -l {username} -P /usr/share/wordlists/rockyou.txt {protocol}://{host} -t 4")
    

# Main
while True:
    choice = menu()
    if choice == "1":
        enumeration()
    elif choice == "2":
        scan_host()
    elif choice == "3":
        brute_force()
    else:
        print("\nPlease type 1, 2, or 3")
    print("")


# End
    
