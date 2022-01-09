## To compile the slave into an executable
### We need the following requirements
* cyphon [https://cyphon.readthedocs.io/en/latest/getting-started/install-cyphon.html]
* gcc [https://gcc.gnu.org/]
* pkg-config [https://www.freedesktop.org/wiki/Software/pkg-config/]
### And then we run the script
* compile.sh [https://raw.githubusercontent.com/trevalkov/ratpy/master/compile.sh]
````bash
#!/bin/bash
PROGNAME=main
PROGPATH=$PWD+src/slave/
cython -3 $PROGPATH+$PROGNAME+.py --embed
gcc $PROGPATH+$PROGNAME+.c -o $PROGNAME $(pkg-config --libs --cflags python3)
rm -f $PROGPATH+$PROGNAME+.c
echo "Compilation complete to ELF binary: $PROGNAME"
````
