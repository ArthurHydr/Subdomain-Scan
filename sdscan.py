# -*- coding: utf-8 -*-
import dns.resolver
import sys

print ""
wordlist = raw_input("Type the wordlist: ")
domain  = raw_input("type the domain: ")
print ""

try:                                              
    arquive = open(str(wordlist))                # open your wordlist
    subdomains = arquive.read().splitlines()     # read lines
except:
    print "Wordlist not found!"
    sys.exit()

for subdomain in subdomains:
    try:
        domesub = subdomain + '.' + domain
        results = dns.resolver.query(str(domain), 'a')
        for results in results:
            print domesub, results
    except:
        pass

