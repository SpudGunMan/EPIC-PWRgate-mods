# EPIC-PWRgate-mods
 West Mountain Radio EPIC PWRgate Mods


/dev/ttyACM0 at 9600 baud

on connect to device it will typically catch the letter 's' string which puts you into setup, handles escaping the menu and handles parsing of data for some other funky text output bugs in firmware
- sol value has extra space
- battery value has extra space
- unplug power supply and the output is ugly so we clean that up

$ python3 [PWRgate-Status.py](PWRgate-Status.py)


```
West Mountain Radio EPIC PWRgate Reporting Tool


Attached to Serial/dev/ttyACM0 Telemetry data:
Traceback (most recent call last):y 14.03V Status TrickleSolar Voltage0.04V


```

```
West Mountain Radio EPIC PWRgate R2 1.32

Press S to Review/Edit Charge settings

Because jumper is installed changes will be reset on next power cycle.

Battery:  1-Disable, 2-Gel, 3-AGM, 4-LiFePo4, 5-Other:    <0>: 
Max charge voltage in Volts:    <14.40>: 
Max charge current in Amps:    <9.98>: 
Min charge current in Amps:    <0.25>: 
Trickle current in Amps:    <0.15>: 
Trickle voltage in Volts:    <13.55>: 
Recharge voltage in Volts:    <12.10>: 
Max charge (minutes):    <1500>: 
Min charger idle (minutes):    <60>: 
Min supply voltage for charging in Volts:    <12.99>: 
Battery Save Mode (Y,N) < N >? 
```