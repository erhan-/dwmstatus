# DWMstatus

## Description

These are two DWM status scripts for my host and for the VMs. They show the hostname, the ip address, time and battery status (only on host).

## Installation

Just copy the desired file to `/usr/bin/` and add the script to `./.xinitrc`.

```
cp dwmstatus_host.py /usr/bin/
chmod +x /usr/bin/dwmstatus_host.py 
```

## Notes

-  Tested on archlinux (host) and centos (vm)
-  The `xrandr` command is a workaround so that "Auto resize VM with window" function in combination with *spice-vdagent* work in DWM.
