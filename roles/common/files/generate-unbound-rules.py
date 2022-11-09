#!/usr/bin/python

import requests

url = 'https://raw.githubusercontent.com/anudeepND/youtubeadsblacklist/master/domainlist.txt'
r = requests.get(url)
r.raise_for_status()

print('server:')

for line in r.text.splitlines():
    print('  local-zone: "{}" redirect'.format(line))
    print('  local-data: "{} A 127.0.0.1"'.format(line))

url = 'https://api.hackertarget.com/hostsearch/?q=googlevideo.com'
r = requests.get(url)
r.raise_for_status()

for line in r.text.splitlines():
    print('  local-zone: "{}" redirect'.format(line))
    print('  local-data: "{} A 127.0.0.1"'.format(line.split(',')[0]))

