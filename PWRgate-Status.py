#!/usr/bin/python
# v1.30 Boilerplate West Mountain Radio EPIC PWRgate Telemetry Script
from serial import *

serialPort = "/dev/ttyACM0" # serial port for linux
baudRate = 9600 # baud rate for device  (9600 is default)

try:
    ser = Serial(serialPort , baudRate, timeout=1, writeTimeout=0) #ensure non-blocking
    ser.flushInput() #flush input buffer, discarding all its contents
    ser.flushOutput() #flush output buffer, aborting current output and discarding all that is in buffer
except:
    print("Failed to connect serial port " + serialPort + ". Exiting...")
    exit()


# initialise variables as strings, for demo purposes
battery=''
power_supply=''
solar_voltage=''
temp=''
status=''
line=''
parsed_line=''
uptime=''

print("\n\nWest Mountain Radio EPIC PWRgate Reporting Tool\n\n")
print("Attached to Serial" + ser.name + " Telemetry data:") #check which port was really used

while True:
    
    if ser.inWaiting() > 0: # check for data on serial port
        line = ser.readline().decode('utf-8').rstrip() # read serial port and decode from binary array to ASCII

        # check for menu which pops up when device is first connected sometimes
        if line.__contains__(':'):
            ser.write('\r'.encode()) # send a carriage return to the device to exit menu
        elif line.__contains__('?'):
            ser.write('n\r'.encode()) # send a 'n' and carriage return to the device to select no
        else: # if not a menu then parse data

            # cleans up some typo in R2 1.32 split line into a list
            parsed_line = line.replace(',  ',',').replace('= ','=').split() 

            # extract values for use
            if len(parsed_line) > 0:
                status = (parsed_line[0])

                if status.__contains__('PS'): # handle when PS is off and not connected
                    status = "Battery-Only"
                    power_supply = (parsed_line[2].replace('PS=',''))
                    battery = (parsed_line[3].replace('Bat=',''))
                    solar_voltage = (parsed_line[4].replace('Sol=',''))
                    uptime = (parsed_line[5].replace('Min=',''))
                    #temp = (parsed_line[5].replace('Temp=',''))
                elif status.__contains__('Bad'): # handle when too hot
                    status = "Temp-Warning"
                    power_supply = (parsed_line[2].replace('PS=',''))
                    battery = (parsed_line[3].replace('Bat=',''))
                    solar_voltage = (parsed_line[4].replace('Sol=',''))
                    uptime = (parsed_line[5].replace('Min=',''))
                    #temp = (parsed_line[6].replace('Temp=',''))
                elif status.__contains__('Charged'): # handle when battery is charged
                    status = "Charged"
                    power_supply = (parsed_line[2].replace('PS=',''))
                    battery = (parsed_line[3].replace('Bat=',''))
                    solar_voltage = (parsed_line[4].replace('Sol=',''))
                    uptime = (parsed_line[5].replace('Min=',''))
                    #temp = (parsed_line[6].replace('Temp=',''))
                else: # handle when PS is on and connected (normal)
                    power_supply = (parsed_line[1].replace('PS=',''))
                    battery = (parsed_line[2].replace('Bat=',''))
                    solar_voltage = (parsed_line[3].replace('Sol=',''))
                    uptime = (parsed_line[4].replace('Min=',''))
                    #temp = (parsed_line[5].replace('Temp=',''))
    else:
        # check for menu which pops up when device is first connected sometimes
        if line.__contains__(':'):
            ser.write('\r'.encode()) # send a carriage return to the device to exit menu
        elif line.__contains__('?'):
            ser.write('n\r'.encode()) # send a 'n' and carriage return to the device to select no

    print("Battery " + battery + " Status " + status + " Power Supply " + power_supply + " Solar Voltage " + solar_voltage, end = "\r") # print to console


ser.close() # close port
