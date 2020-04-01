import obd
import csv
from datetime import datetime
import time

# obd.logger.setLevel(obd.logging.DEBUG) # Enables Debugger
try:
	print("Connecting with ODB Serial/COM")
	a= obd.scan_serial()
	connection = obd.OBD(a[0],baudrate=10400, fast=False) #Connecting with Serial/COM
except Exception as e:
	print(e)
spd = obd.commands.SPEED
rpm = obd.commands.RPM
thr = obd.commands.THROTTLE_POS
i=0

with open('speed.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Time", "Speed","RPM","Throttle"])
	while(i<100):	
		#speed
		speed = connection.query(spd)
		speed_value=float(speed.replace(' kph', ''))
		#rpms
		rpms  = connection.query(rpm)
		rpms_value =float(rpms.replace(' revolutions_per_minute', ''))
		#throttle
		thrr  = connection.query(thr)
		thrr_value =float(rpms.replace(' percent', ''))
		if(response != None):
			print(speed.value,rpms.value,thrr.value)
			print()
			now = datetime.now()
			writer.writerow([datetime.timestamp(now),speed.value,rpms.value,thrr.value])
		i=i-1
		time.sleep(2) #Delay for 2 sec


