# CarAssistant
Car monitoring and tracking tools to be run from a Raspberry Pi (or other small linux computer)

# Planned Modules
### GPS
  Track car location, handy for a handful of use cases.
### OBD2
  Get car metrics such as speed, fuel usage, RPM, throttle, temperture, gear selection, manifold pressure, other fun stuff for those tuners out there. (Even though you probably have a good reader already)
### Battery
  Rechargeable battery that will charge while the car is on and allow the system to operate for some time after the car is off. This can be useful to track your wonderful car in the case of theft by goons or towing by vermin.
### 3G/4G Data Connection
  Get maps and send out data wherever you are!
### WiFi
  If your home wifi is able to reach your car, allow the car to connect to your network and then allow ssh or automate some data transfer. This might be handy with the battery module to allow transfers to happen without the engine being on.
### Home Assistant
  Integrate into Home Assistant as a device_tracker style integration to allow reporting of location and other metrics like fuel and speed. Then you can make automations to remind you to gas up or that during rush hour you never went above 15 MPH. The Cell Data Connection module would be nearly essential for this.
