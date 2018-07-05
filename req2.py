import requests
import sys

print(sys.argv)

domain = sys.argv[1]
show = requests.get("https://"+domain).status_code
print(show)
