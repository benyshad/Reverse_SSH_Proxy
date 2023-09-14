#!/usr/bin/env python3
#this script sets up the proxy using the command 'ssh -D'
from datetime import datetime
import os
import subprocess as sp

whoami = "notpi"
#if the proxy is already connected and working properly the command 'whoami' will
#return pi. but if the proxy is connected then it will return shadownet
#run the command 'whoami' on the screen proxy and return the output into a txt
os.system("screen -S proxy -X stuff 'whoami > whoami.txt\\n'")
#set a variable to the output
whoami = sp.getoutput('cat whoami.txt')
os.system("screen -S proxy -X stuff 'rm whoami.txt\\n'")

#if the output is shadownet, then the proxy is not connected
if whoami == 'shadownet':
    #get the date and time
    nowint = datetime.now()
    #make the date and time into a readble format
    nowstr = nowint.strftime('%Y-%m-%d %I:%M:%S %p')
    #log the date and time
    filelog = open("shadownetproxylog.txt", "a")
    filelog.write(nowstr + "\n")
    filelog.close()
    #start the proxy using the "ssh -D" which will start a proxy on port 10326
    #over the ssh connection to the pi server
    os.system("screen -S proxy -X stuff 'ssh -D 10326 piproxy\\n'")

#if the output is pi, then the proxy is connected and is working properly
else:
    print("connected")
