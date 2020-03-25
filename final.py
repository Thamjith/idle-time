# this is a program to observe and report the idle time of the computer in which it is running

from idle_time import IdleMonitor
import datetime
from gi.repository import Notify
import matplotlib.pyplot as graph


maxIdleTime = 10 #enter the idle time in minutes
#maxIdleTime*=60 #If you comment this line you will get seconds
shiftStartTime = datetime.datetime.now()
shiftTimeEnd = datetime.datetime.strptime('22:00:00', '%H:%M:%S').time() #In 24 hour format
monitor = IdleMonitor.get_monitor()
graphDataX = []
graphDataY = []
filename = datetime.datetime.now()
f= open("%s.txt"%(filename),"w+")
graph.show()
while True:
	print(monitor.get_idle_time())
	# if datetime.datetime.now().time() >= shiftTimeEnd:
	# 	break
	if datetime.datetime.now() >= shiftStartTime + datetime.timedelta(minutes = 1):
		break
	flag1 = 1
	flag2 = 0
	totalIdledTime = 0
	idleStartTime = datetime.datetime.now().time()
	while monitor.get_idle_time() > 1:
		print("---" + str(monitor.get_idle_time()))
		if monitor.get_idle_time() >= maxIdleTime:
			if monitor.get_idle_time() > totalIdledTime:
				totalIdledTime = monitor.get_idle_time()
			if flag1:
				f.write("The user has been idling for %s minutes from %s to %s\n\n" % (maxIdleTime, idleStartTime, datetime.datetime.now().time()))
				flag1 = 0
				flag2 = 1
				# notification for linux
				Notify.init("App Name")
				Notify.Notification.new("You have been Idling for %s minutes" %(maxIdleTime)).show()

				# graph.plot(graphDataX, graphDataY)
				# graph.xlabel('idle')
				# graph.ylabel('time')
				# graph.title('Users Idle time') 
				# graph.show()
	if flag2:
		graphDataX.append(datetime.datetime.now())
		graphDataY.append(totalIdledTime)
		f.write("	The user has idled for %s minutes\n" % (totalIdledTime))
		f.write("%s " % (graphDataX))
		f.write("%s \n---------------------------------------\n" % (graphDataY))
		Notify.uninit()
f.close