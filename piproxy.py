#!/usr/bin/env python3

#he point of this script is to open a dedicated reverse shell to run the proxy on
#the point of using a dedicated reverse shell is so that if for some reason the proxy fails
#i still have another reverse shell the should be working properly
#this script is meant to be run on the pi
from datetime import datetime
import os
import subprocess as sp

whoami = "notpi"
#if the reverse shell is connected the whoami command will return local_server
#if its now connected then it will return pi
#run the whoami command on the screen proxy and save the output to a txt file
os.system("screen -S proxy -X stuff 'whoami > whoami.txt\\n'")
#assign a variable to the output of the 'whoami' command
whoami = sp.getoutput('cat whoami.txt')
os.system("screen -S proxy -X stuff 'rm whoami.txt\\n'")

#if whoami is = to pi that means the reverse connection isnt established
if whoami == 'pi':
    #log the date and time
    nowint = datetime.now()
    #make the date and time into a readable format
    nowstr = nowint.strftime('%Y-%m-%d %I:%M:%S %p')
    # add it to the log file
    filelog = open("piproxylog.txt", "a")
    filelog.write(nowstr + "\n")
    filelog.close()
    #start the reverse shell
    os.system("screen -S proxy -X stuff 'ssh -R 26:localhost:3626 local_server\\n'")

#if whoami returns local_server then the reverse connection is established
else:
    print("connected")
    print("pi proxy")
    print(whoami)
