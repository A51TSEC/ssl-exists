import requests
import sys
from sys import argv



domain=sys.argv[1]
https_check = requests.get("https://"+domain)
checker = https_check.status_code
if checker == 200:
    print('Using SSL certificate')
else:
    print('No SSL certificate')
