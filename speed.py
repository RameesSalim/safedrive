import obd
import csv
import time


obd.logger.setLevel(obd.logging.DEBUG) # Enables Debugger
try:
	print("Connecting with ODB Serial/COM")
	connection = obd.OBD('/dev/tty.OBDII-SPPslave') #Connecting with Serial/COM
except Exception as e:
	print(e)
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Speed"])
cmd = obd.commands.SPEED
i=0

while(i<100):	
	response = connection.query(cmd)
	print(response.value)
	i=i-1
	time.sleep(.2) #Delay for .2 sec
	with open('data.csv', 'w', newline='') as file:
    	writer = csv.writer(file)
   		writer.writerow([timedate.now(), response.value])


