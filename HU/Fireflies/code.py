import urllib.request as r
import requests
import certifi
import ssl

url = 'https://host-en28hrdw-prod.prod.cywar.xyz:49379/'

page  = requests.get(url, data, verify=False,)

print(page.getcode())
