#!/bin/python3

import subprocess
import re
import socket
import shlex
from datetime import datetime
from time import sleep

acpi_regex = r"([\w]+), ([\d]{1,2})%, ([\d:]*)"

while True:
    acpi_output = subprocess.check_output(['acpi']).decode("utf-8") 
    acpi_match = re.search(acpi_regex, acpi_output)
    if acpi_match:
        mode = acpi_match.group(1)
        battery_percentage = acpi_match.group(2)
        time_remaining = acpi_match.group(3)
        status_icon = '+' if mode == 'Charging' else '-'
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(socket.gethostname())
        status_string = f"{hostname}({ip_address}) | {now} | [{status_icon}] {battery_percentage}% ({time_remaining})"
        subprocess.call(['xsetroot', '-name', shlex.quote(status_string)])
    sleep(5)
