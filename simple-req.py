import requests
from sys import argv
import sys



domain=sys.argv[1]
try:
    a=requests.get('https://'+domain, verify=True)
    print ("SSL exists on website")
except:
    print("Domain may be down")
