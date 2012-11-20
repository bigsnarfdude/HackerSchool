import re
import cPickle as pickle
import datetime
import xml.etree.ElementTree as ET
from commands import getoutput
import re, urllib2, webbrowser
import json as simplejson

command = 'nmap -T4 -A -p 1-1000 -oX -  localhost'


def get_nmap_output():
        

root = ET.fromstring(getoutput(command))
root.tag
tree.attrib
tree.getchildren()
elements = tree.getchildren()
elements[0]
elements[1]
elements[2]
elements[3].tag
description = tree.attrib
description['version']
host_info.getchildren()
host_info.getchildren()[2]
hostnames = host_info.getchildren()[2]
hostnames[0].attrib['name']
target = hostnames[0].attrib['name']
target
