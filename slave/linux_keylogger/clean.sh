#!/bin/sh
sudo killall keylogger
cat /tmp/keylog.txt
rm -f /tmp/keylog.txt
cd src && rm -f keylogger

