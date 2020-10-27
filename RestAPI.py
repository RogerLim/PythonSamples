#!/usr/bin/python3

import requests
import json

parameters = {
    "lat": 1.17,
    "lon": 103.51
}

def jprint(obj):
    # Create a formatted string of Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

body = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print("\n\nStart of execution...\n")
jprint(body.json())

pass_times = body.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
