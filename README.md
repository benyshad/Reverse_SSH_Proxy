# Reverse SSH Proxy


## Proxy Over A Reverse SSH Shell


## Description

This project was to create a proxy over a reverse ssh shell created in a different project. The goal was to have the internet traffic coming through the remote server. As mentioned in the other project, port forwarding was not possible for the remote server and I therefore needed a reverse ssh shell. A OpenVPN was not either an option, being that OpenVPN would also require port forwarding. To achieve a connecting between the user's desktop / laptop and the proxy, I first needed to bind a local port on the users computer to a port on a local server using ssh. Then through the reverse ssh shell to the remote server a socks5 proxy was setup on the same port using ssh.


## Usage
The piproxy.py file is placed on the remote server where port forwarding is accessible.
local_server.py is placed on the local server where port forwarding is accessible.
And proxy.sh is run on the local machine.
Just by running the proxy.sh on the local machine the other 2 scripts are run automatically.
```bash
./proxy.sh
```
