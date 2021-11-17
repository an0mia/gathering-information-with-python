import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print('usage:\n' + sys.argv[0] + ' <url>')
    sys.exit(1)

req = requests.get('https://' + sys.argv[1])
print('\n' + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print('\nipaddress: ' + gethostby_+ '\n')

#api robtex
req2 = requests.get('https://freeapi.robtex.com/ipquery/' + gethostby_)
resp_ = json.loads(req2.text)

print('status: ' + resp_['status'])
print('country: ' + resp_['country'])
print('city: ' + resp_['city'] + '\n')
print('asname: ' + resp_['asname'])
print('whoisdesc: ' + resp_['whoisdesc'])
print('routedesc: ' + resp_['routedesc'])
print('bgproute: ' + resp_['bgproute'])
print() 
quit()


