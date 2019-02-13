# pythongit
Sample code in python

REQUEST IP
```
import json
import requests

resp = requests.get('https://ipinfo.io/json')
print(resp.json())
print(resp.json()['ip'])
```
