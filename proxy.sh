#!/bin/sh

#logon to the pi server and run the piproxy.py script which will start a dedicated
#ssh connection for the proxy
ssh -J local_server pi ./piproxy.py
#sleep 3 seconds to give time for the pi to establish a connection
sleep 3
#log on to local_server and establsh the proxy
ssh local_server ./local_serverproxy.py
#kill the screen named proxy that was perviously binding the local port 10326
#to the port 10326 on local_server which is the port that the proxy is running on
screen -S proxy -p 0 -X quit
#creat a new screen named proxy
screen -d -m -S proxy
#bind the local port 10326 to the port 10326 of local_server. Port 10326 on local_server
#the port that the proxy is runing on
screen -S proxy -X stuff "ssh -L 10326:localhost:10326 local_server\\n"
