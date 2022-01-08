#!/bin/bash
PROGNAME=main
PROGPATH=$PWD+src/slave/
cython -3 $PROGPATH+$PROGNAME+.py --embed
gcc $PROGPATH+$PROGNAME+.c -o $PROGNAME $(pkg-config --libs --cflags python3)
rm -f $PROGPATH+$PROGNAME+.c
echo "Compilation complete to ELF: $PROGNAME"
