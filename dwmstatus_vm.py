#!/bin/python3

import subprocess
import re
import socket
import shlex
from datetime import datetime
from time import sleep

while True:
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
    except:
        ip_address = "127.0.0.1"
    status_string = f"VM: {hostname}({ip_address}) | {now}"
    subprocess.call(['xsetroot', '-name', shlex.quote(status_string)])
    subprocess.call(['xrandr', '--output', 'Virtual-0', '--auto'])
    sleep(5)
