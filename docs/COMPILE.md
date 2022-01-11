## To compile the slave into an executable
### We need the following requirements
* cyphon [https://cyphon.readthedocs.io/en/latest/getting-started/install-cyphon.html]
* llvm [https://llvm.org/]
* gcc [https://gcc.gnu.org/]
* pkg-config [https://www.freedesktop.org/wiki/Software/pkg-config/]
* docker
### And then we run the script
This program was built to run on Linux and BSD
So to compile it from a different OS or architecture
We can use a virtual image from here
* dockcross [https://github.com/dockcross/dockcross]
Transpile from Python to C using cyphon locally
Then compile it using the docker image
````bash
#!/bin/bash
PROGNAME=main
PROGPATH=$PWD+src/slave/
cython -3 $PROGPATH+$PROGNAME+.py --embed
gcc $PROGPATH+$PROGNAME+.c -o $PROGNAME $(pkg-config --libs --cflags python3)
rm -f $PROGPATH+$PROGNAME+.c
echo "Compilation complete to ELF binary: $PROGNAME"
````
