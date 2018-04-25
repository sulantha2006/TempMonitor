#!/bin/bash

####   python /home/pi/TempMonitor/CheckTemp.py > /home/pi/TempMonitor/TempMonitor.log 2>&1 &
/home/pi/miniconda3/bin/python -u /home/pi/TempMonitor/CheckTemp.py 2>&1 > /home/pi/TempMonitor/TempMonitor.log &
# until ping -c 1 -W 1 8.8.8.8; do sleep 1; done
/home/pi/miniconda3/bin/python -u /home/pi/TempMonitor/RunService.py 2>&1 > /home/pi/TempMonitor/Service.log &
#  python /home/pi/TempMonitor/CheckTemp.py
