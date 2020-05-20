#!/bin/python3

import subprocess
import re
import socket
import shlex
from datetime import datetime
from time import sleep

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

while True:
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    hostname = socket.gethostname()
    ip_address = get_ip_address()
    status_string = f"VM: {hostname}({ip_address}) | {now}"
    subprocess.call(['xsetroot', '-name', shlex.quote(status_string)])
    subprocess.call(['xrandr', '--output', 'Virtual-0', '--auto'])
    sleep(2)
