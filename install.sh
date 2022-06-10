#!/data/data/com.termux/files/usr/bin/bash
cd
pkg update -y
pkg upgrade -y
pkg install git python -y
git clone https://github.com./arminhere/MyScripts
cd MyScripts
pip install requests
echo Use python sms.py to execute the sms bomb. cntrl+C to stop
