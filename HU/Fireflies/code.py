import urllib.request as r
import certifi

page = r.urlopen('https://host-vziwab7a-prod.prod.cywar.xyz:49194/', cafile=certifi.where())
print(page.getcode())
