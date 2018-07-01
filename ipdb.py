#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------
#   Ip Database filler utility v1.0
#------------------------------------------
import time
import argparse
import dataset
from stuf import stuf
from ipwhois import IPWhois


# Parse the arguments used in this script
parser = argparse.ArgumentParser(description='Example with non-optional arguments')
parser.add_argument('-ip', action="store", type=str, dest='ip')
parser.add_argument('-country', action="store", type=str, dest='country')
parser.add_argument('-sleep', action="store", type=int, dest='timesleep')

results = parser.parse_args()
countrylist = open('country.txt', 'r').read().split('\n')

db = dataset.connect('sqlite:///ipdatabaseipv4.db', row_type=stuf)
whoisdb = db['ipdb']

#Fill the ip database
def whois_ip(ip):
    try:
        # Get whois for IP. Returns a list with dictionary
        obj = IPWhois(str(ip))
        results = obj.lookup_whois(inc_nir=True)
        name = results['nets'][0]['name']
        description = results['nets'][0]['description']
        cidr = results['nets'][0]['cidr']
        data = dict(ipstart=ip, name=name, description=description, cidr=cidr)
        whoisdb.upsert(data, ['ipstart'])
        time.sleep(timesleep)
        print cidr,name,description
    except Exception as e: print(e)

# Make the ip list
def iprange(rangeStartSring,country):

    ipr={}
    findrange = whoisdb.find(country=country)
    for ipstartrange in findrange:
        if ipstartrange['cidr'] is None:
            if rangeStartSring !='':

                if ipstartrange['ipstart'].startswith(rangeStartSring):
                    ipr[ipstartrange['ipstart']]=ipstartrange['ipstop']
            else:
                ipr[ipstartrange['ipstart']] = ipstartrange['ipstop']
        else:
            pass
    for whoischeck in ipr:
        whois_ip(whoischeck)

# Setup the parameters
if results.ip is not None and results.country is not None:
    if results.country in countrylist:
        iprange(results.ip, results.country)
    if results.country == "ALL":
        for allcountries in countrylist:
            iprange(results.ip, allcountries)
    else:
        print 'The country code is invalid'
if results.timesleep is not None:
    timesleep = results.timesleep
if results.timesleep is None:
    timesleep = 1
    print 'Timesleep set to 1'
if results.country is not None:
    if results.country in countrylist:
        iprange('', results.country)
    if results.country == 'ALL':
        for allcountries in countrylist:
            iprange('',allcountries)
    else:
        print 'The country code is invalid'

if results.country is None and results.ip is None:
    print 'Ip Database filler utility v1.0'
    print ''
    print '-------------------------------------------------------------------------------------------------------------'
    print '*********************************Fill the database with whois information************************************'
    print '-------------------------------------------------------------------------------------------------------------'
    print 'Example usage'
    print 'ipdb.py -ip 200. -country US (scan all the US ip address starting with 200.)'
    print 'Note: You can also use a more narrow range like 200.62.21. '
    print 'ipdb.py -country US  (scan all the US ip ranges... Maybe a bad idea)'
    print 'ipdb.py -country ALL -ip 200 -sleep 5 (scan all the ip starting with 200. and wait 5 seconds between requests)'
    print 'ipdb.py -country ALL (scan all the ip ranges... This will take it forever :P )'

    #iprange('159','GB')

    #countryListMaker()