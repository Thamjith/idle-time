# this is a program to observe and report the idle time of the computer in which it is running

from idle_time import IdleMonitor
import datetime
from gi.repository import Notify
import matplotlib.pyplot as graph
import time
from cryptography.fernet import Fernet
import pyfiglet 


maxIdleTime = 1 #enter the idle time in minutes
maxIdleTime *= 60 #If you comment this line you will get seconds
shiftStartTime = datetime.datetime.now()
shiftEndTime = datetime.datetime.strptime('19:14:00', '%H:%M:%S').time() #In 24 hour format
monitor = IdleMonitor.get_monitor()
graphDataX = [datetime.datetime.now().strftime('%H:%M:%S')]
graphDataY = [0]
filename = datetime.datetime.now()
f= open("%s.txt"%(filename),"w+")
f.write("Users Idle time on %s\n--------------------------------------\n" %(datetime.datetime.now().strftime('%a, %d:%B:%Y')))
plainText = "Users Idle time on %s\n--------------------------------------\n" %(datetime.datetime.now().strftime('%a, %d:%B:%Y'))
print("***Program is running***\n***DO NOT CLOSE THIS TERMINAL***")
print(pyfiglet.figlet_format("I D L E\n", font = "3-d"))
print(pyfiglet.figlet_format("T I M E\n", font = "3-d"))
def graphValueUpdate():
	graphDataX.append(datetime.datetime.now().strftime('%H:%M:%S'))
	graphDataY.append(totalIdledTime)
def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec)
Notify.init("App Name")
Notify.Notification.new("The program started...").show()
Notify.uninit()
while True:
	#print(monitor.get_idle_time()) #comment this line if no feedback is needed
	if datetime.datetime.now().time() >= shiftEndTime:
		break
	flag1 = 1
	flag2 = 0
	totalIdledTime = 0
	idleStartTime = datetime.datetime.now().strftime('%H:%M:%S')
	while monitor.get_idle_time() > 1:
		#print("---" + str(monitor.get_idle_time())) #comment this line if no feedback is needed
		if datetime.datetime.now().time() >= shiftEndTime:
			break
		if monitor.get_idle_time() >= maxIdleTime:
			if monitor.get_idle_time() > totalIdledTime:
				totalIdledTime = monitor.get_idle_time()
			if flag1:
				flag1 = 0
				flag2 = 1
				graphDataX.append(datetime.datetime.now().strftime('%H:%M:%S'))
				graphDataY.append(0)
				graphValueUpdate()
				# notification for linux
				Notify.init("App Name")
				Notify.Notification.new("You have been Idling for %s minutes" %(maxIdleTime/60)).show()
				Notify.uninit()
		time.sleep(1)
	if flag2:
		graphValueUpdate()
		graphDataX.append(datetime.datetime.now().strftime('%H:%M:%S'))
		graphDataY.append(0)
		f.write(" -> The user has idled for %s duration from %s to %s\n" % (convert(totalIdledTime), idleStartTime, datetime.datetime.now().strftime('%H:%M:%S')))
		plainText += " -> The user has idled for %s duration from %s to %s\n" % (convert(totalIdledTime), idleStartTime, datetime.datetime.now().strftime('%H:%M:%S'))
	time.sleep(1)
f.close
graphDataX.append(datetime.datetime.now().strftime('%H:%M:%S'))
graphDataY.append(0)
graph.plot(graphDataX, graphDataY)
graph.xlabel('time', fontsize='small')
graph.xticks(rotation=25)
graph.ylabel('idle (in seconds)')
graph.title("Users Idle time on %s" %(datetime.datetime.now().strftime('%a, %d:%B:%Y'))) 
graphName = str(datetime.datetime.now())
graphName += ".png"
graph.savefig("%s" %(graphName))
Notify.init("App Name")
Notify.Notification.new("Your shift ended, bye...").show()
Notify.uninit()
g = open("encrypt.txt","w+")
encodedPlainText = plainText.encode()
cipher_suite = Fernet(b'N0oW_ObT2SxvI2wiwBFX0FGjvN70WfAoNIaeksl4t08=')
cipherText = cipher_suite.encrypt(encodedPlainText)
cipherText = str(cipherText, 'utf-8')
g.write(cipherText)
g.close
print("|--------------------|\n")
print("| Your shift is over |\n")
print("|--------------------|")
