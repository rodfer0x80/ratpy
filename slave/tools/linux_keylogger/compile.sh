#!/bin/sh
cd src && gcc -g -Wall -Wextra linux_keylogger.c -o keylogger && mv keylogger ..
