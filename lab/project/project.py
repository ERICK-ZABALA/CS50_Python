#!/usr/local/bin/python
from dotenv import load_dotenv
import os
import requests
import json
import nmap
import cowsay
import random
from pyfiglet import Figlet
import sys
import re

def main():

    ip_address = get_interface()
    print("IP Address: ",ip_address)
    get_nmap_scanner(ip_address)
    get_location(ip_address)

def validate(ip_address):

    try:
        if (re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_address)):
            numbers = ip_address.strip().split(".")
            numbers = [int(i) for i in numbers]
            for x in numbers:
                if str(x).isdigit():
                    print()
                else:
                    return False

            counter = 0
            for x in numbers:
                if (x > -1) and (x < 256):
                    counter = counter + 1
            if counter == 4:
                return True
            else:
                return False
        else:
            return False

    except ValueError:
        sys.exit(1)

def get_interface():
    try:
        if (len(sys.argv) > 1) and (sys.argv[0] == "project.py"):
            print ("Invalid usage")
            sys.exit(1)
        else:
            print(cowsay.get_output_string(cowsay.char_names[random.randint(0,18)], ".... H31l0 NM@P and AP! ..!"))
            get_design()
            ip_address = input("What is the Ip Address? (target): ").strip()
            found = validate(ip_address)
            # print(bool(found))
            if (bool(found) == True):
                return ip_address
            else:
                print ("Invalid usage")
                sys.exit(1)

    except IndexError:
        sys.exit()

def get_design():
    message = "Nmap & Location"
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font = "slant")
    print(figlet.renderText(message),end= "")


def get_nmap_scanner(ip_address):
    scanner = nmap.PortScanner()

    print("Namp Version:", scanner.nmap_version())
    info = scanner.scan(ip_address,sudo='sudo',arguments='-Pn',ports='1-9090')

    print("Ip Status: ",scanner[ip_address].state())
    if scanner[ip_address].state() == "down":
        print ("Verify Ip Address is not possible scan port...!")
        sys.exit(1)

    print("===============================================================")
    for port in scanner[ip_address]['tcp'].keys():
        for protocol in scanner[ip_address].all_protocols():
            print("Protocol: ", protocol)

        print("Open Port: ", port)
        print("State Listen: ", scanner[ip_address]['tcp'][port]['state'])
        print("Type Service: ", scanner[ip_address]['tcp'][port]['name'])
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def get_location(ip_address):

    API_KEY = os.getenv("API_KEY")
    load_dotenv()

    IP_ADDR = ip_address
    url = f"http://api.ipstack.com/{IP_ADDR}?access_key={API_KEY}"

    response = requests.get(url)
    location = response.json()

    try:
        if location["success"] == False:
            print ("Verify your API Key stay in your system export..., that is not valid!")
            sys.exit(1)
    except KeyError:
        pass

    country = location["country_name"]
    city = location["city"]
    latitude = location["latitude"]
    longitude = location["longitude"]

    print(f"Location Target: {ip_address}\nCountry:  {country}\nCity: {city}\nLatitude: {latitude}\nLongitude: {longitude}")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


if __name__=='__main__':
    main()