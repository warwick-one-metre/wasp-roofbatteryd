## SuperWASP roof battery monitor daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/wasp-roofbatteryd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/wasp-roofbatteryd)

`roofbatteryd` recieves data from [a custom usb voltmeter](https://github.com/warwick-one-metre/wasp-battery-meter) and
makes the latest measurement available for other services via Pyro.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup

After installing `wasp-roofbattery-server`, the `roofbatteryd` must be enabled using:
```
sudo systemctl enable wasp_roofbatteryd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start wasp_roofbatteryd.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9017/tcp --permanent
sudo firewall-cmd --reload
```

### Hardware Setup

The [usb voltmeter](https://github.com/warwick-one-metre/wasp-battery-meter) is matched against its unique serial number.  If the Arduino is replaced then the serial number should be updated in `10-wasp-roofbattery.rules`.
