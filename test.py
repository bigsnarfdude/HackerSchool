#!/usr/bin/env python
# Julien Deudon (initbrain) - 20/03/2012 15h35
# modified to english version by Dan Gleebits 20/06/2012
# modified to run on OS X by James Armitage 25/06/2012
# modified to process in python Dan Gleebits 26/06/2012
# parsing xml Vincent Ohprecio 01/10/2012

# import all the necessary libraries
from commands import getoutput
import re, urllib2, webbrowser
import json as simplejson
import xml.etree.ElementTree as ET
# bash command to grab the neighboring wifi data around the laptop
airport_scan_xml = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport --scan -x'
# regular expression to match MAC address
macMatch = '([a-fA-F0-9]{1,2}[:|\-]?){6}'
# running network WiFi scan
print "[+] Scanning network"
tree = ET.parse(airport_scan_xml)
root = tree.getroot()
mac_address = ''
signal_strength = 0
for level_1 in root:
  for level_2 in level_1:
    for level_3 in level_2.findall('string'):
      if re.compile(macMatch).search(level_3.text):
        mac_address = level_3.text
    for level_3 in level_2:
      if "NOISE" in level_3.text:
        flag = 2	    
      if "RSSI" in level_3.text:
        flag = 1
      if len(level_3.text) < 4:
        try:
          signal_number = int(level_3.text)
          if signal_number < 0:
            final_signal_strength = abs(int(level_3.text))
          if flag == 1:
            signal_strength = final_signal_strength
        except:
          pass
      if "SSID" == level_3.text:
        flag = 0
    print mac_address, signal_strength





print "[+] Creating HTML request"
locationRequest={
		"version":"1.1.0",
		"request_address":False, 
		"wifi_towers":[{"mac_address":"00-00-00-00-00-00","signal_strength":0}],
		}


        tempDict = {"mac_address":x.split()[1].replace(":","-"),"signal_strength":abs(int(x.split()[2]))}
        locationRequest["wifi_towers"].append(tempDict)

           
# this takes the cleaned up data and serialize to JSON request for Google API
print "[+] Sending the request to Google"
data = simplejson.JSONEncoder().encode(locationRequest)
output = simplejson.loads(urllib2.urlopen('https://www.google.com/loc/json', data).read())

# prints out the latitude and longitute data returned from Google and opens browser to visually location MAC
print "[+] Google Map"
print "http://maps.google.com/maps?q="+str(output["location"]["latitude"])+","+str(output["location"]["longitude"])
googleMapWebpage = "http://maps.google.com/maps?q="+str(output["location"]["latitude"])+","+str(output["location"]["longitude"])
webbrowser.open(googleMapWebpage)