import subprocess
import json
import os

wifidata = subprocess.check_output(["netsh","wlan", "show", "profiles"]).decode(encoding="utf-8").split("\n")
wifionly = [line.split(":")[1][1:-1] for line in wifidata if "All User Profile" in line ]
allWifiInfo = {}
index = 0
for wifi in wifionly:
    passwords = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode(encoding="utf-8").split("\n")
    IdWifi = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode(encoding="utf-8").split("\n")
    IdWifi = [line.split(":")[1][1:-1] for line in IdWifi if "All User Profile" in line][index]
    password  = [line.split(":")[1][1:-1] for line in passwords if "Key Content" in line ][0] 
    index = index + 1
    try:
        allWifiInfo[IdWifi] = password
    except: 
        allWifiInfo[IdWifi] = "Password Cannot Be found"

with open(os.getcwd() + "/WifiPasswordExtractorAndSendIT/result.txt","w") as fuf:
    fuf.write(json.dumps(allWifiInfo))
    
print("Done yak ")

