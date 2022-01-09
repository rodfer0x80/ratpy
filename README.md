# ratpy
<p align="left">
<img src="imgs/ratpy.png" width="160" height="160">
</p>

> another snake friendly rat backbone

### _________________________________________________________________________
## Architecture
````
This is a backbone build with scripts and space for tools
Before deploying and starting client change the port and server ip address for your server 
Start server listening up to 20 connections with a simple menu interface in the terminal
Client will background by forking twice and killing parents and trying to obfuscate itself 
If client fails it will respawn forever which might crash the system after a while but wont start on reboots
Encryption is done using AES256 from the pycryptodome library
Communications is done via socket connection of byte array type
Once connection is estabilished we have a default set of commands, for basic IO control and dropping a shell
````

### Master
````
* interface - server menu and server cli scripting
* threadpool - running paralel code to serve menu while waiting 
  and handling connections set to up to 20 by default
* tools - backdoor :: encrypted reverse shell
  30s RAT connection with respawn and client-side
* utils - encryption methods and connection methods
````

### Slave
````
* interface - client cli scripting
* tools - RAT client backdoor
* utils - encryption methods and connection methods
> server :: python3 obfuscator.py && <copy ratpy.py to slave machine>
````

### Todo
````
[x] Swap xor for AES256 encryption
[x] Client compilation
[x] Encryption tests
[ ] Server logger
[ ] Client OS enumeration
````

### _________________________________________________________________________
## Disclaimer
````
This project provides a prototype to build on top of and educational purposes.
See license in LICENSE :: GPL3.0 [https://raw.githubusercontent.com/trevalkov/ratpy/master/LICENSE]
````
