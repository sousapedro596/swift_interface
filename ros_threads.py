#!/usr/bin/python3.4
from threading import Thread 
import time
import queue 
from helloworld import Ui_MainWindow
import reSetupUi
from PyQt4 import QtCore, QtGui
import sys
import qgmap
import socket

# Ssh sconnection
import paramiko

import LatLon23


#SWIFT_IP = "192.168.43.23"
SWIFT_IP = "192.168.43.178"
SWIFT_USERNAME = "odroid"
SWIFT_PASSWORD = "odroid"


UDP_IP = SWIFT_IP
UDP_SEND_PORT = 5005
UDP_RECV_PORT = 5006

interface_queue = queue.Queue()

message = bytes("message", "utf-8")




#Subclassing the UI subclass and add custom features to the generated UI
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)


		self.lat  =  []
		self.lon =  []
		self.mission_velocity = 0.2 
		self.swift_lat = 0
		self.swift_lon = 0
		self.alive = 1
		self.markers_list = []
		self.connection_lost_indicator = 0
		self.robot_connected = 0


		self.btn_send_clicked = 0
		self.btn_stop_clicked = 0
		self.btn_start_clicked = 0
		
		self.setupUi(self)
		self.setupButtons()
		self.setupMaps()
		self.setupTimer()


	

	#SSH Thread
	def ssh(self):

		self.ssh_established= 0

		while self.alive == 1:

			if self.robot_connected == 1 and self.ssh_established== 0:

				#setup a general purpose ssh connection and keep it alive
				self.client = paramiko.SSHClient()
				self.client.load_system_host_keys()
				self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				self.client.connect(SWIFT_IP, username=SWIFT_USERNAME, password=SWIFT_PASSWORD)
				stdin, stdout, stderr = self.client.exec_command('source /home/odroid/catkin_ws/devel/setup.bash')
				
				self.ssh_established = 1

			elif self.robot_connected == 0:
				self.ssh_established= 0

			#elif self.ssh_established== 1:
			# try ping and handle roundtrip delay value

			time.sleep(0.5) 


		#Try to disconnect from ssh if it's still active
		try:
			self.client.close()

		except AttributeError:
			pass
	

		# #self.client.close()	


	def setupButtons(self):
		self.pushButton_6.clicked.connect(self.btn_clearAll)
		self.pushButton_13.clicked.connect(self.btn_safety_stop)
		self.pushButton_8.clicked.connect(self.btn_arm)
		self.pushButton_9.clicked.connect(self.btn_set_mode_offboard)
		self.pushButton_7.clicked.connect(self.btn_start_offboard)
		self.pushButton_12.clicked.connect(self.btn_set_mode_offboard)
		self.pushButton.clicked.connect(self.btn_send_mission)
		self.pushButton_2.clicked.connect(self.btn_start_mission)
		self.pushButton_3.clicked.connect(self.btn_stop_mission)


	def btn_stop_mission(self):
		self.btn_stop_clicked = 1

	def btn_start_mission(self):
		self.btn_start_clicked = 1


	def btn_send_mission(self):
		self.btn_send_clicked = 1


	def btn_start_offboard(self):

		if self.ssh_established == 1:
			stdin, stdout, stderr = self.client.exec_command('python /home/odroid/SWIFT/offboard.py ')	
		else:
			print("ssh not available yet")

	def btn_arm(self):
		if self.ssh_established == 1:
			stdin, stdout, stderr = self.client.exec_command('source /home/odroid/catkin_ws/devel/setup.bash && rosrun mavros mavsafety arm')	
		else:
			print("ssh not available yet")

	def btn_set_mode_offboard(self):
		if self.ssh_established == 1:
			self.client.exec_command("source /home/odroid/catkin_ws/devel/setup.bash && rosrun mavros mavsys mode -c OFFBOARD")
		else:
			print("ssh not available yet")			


	def btn_set_mode_manual(self):
		if self.ssh_established == 1:
			self.client.exec_command("source /home/odroid/catkin_ws/devel/setup.bash && rosrun mavros mavsys mode -c MANUAL")
		else:
			print("ssh not available yet")
		
	def btn_clearAll(self):
		
		#clear the table
		self.tableWidget.setRowCount(0)
		
		#delete all markers (create a function if used twice)
		for x in range(1, len(self.lat)+1):
			self.gmap.deleteMarker(x)

		#Cleaning coords vars
		self.lat = []
		self.lon = []
	

		#set 0 to markers count
		self.markers_count = 0

	def btn_safety_stop(self):
		if self.ssh_established == 1:		
			stdin, stdout, stderr = self.client.exec_command('source /home/odroid/catkin_ws/devel/setup.bash && rosrun mavros mavsafety disarm')
		else:
			print("ssh not available yet")


	def setupTimer(self):
		''' Setup a general usage 1 sec timer  '''
		#timer reference to keep it alive when the setup timer function ends
		self.timers = []
		timer = QtCore.QTimer()
		timer.timeout.connect(self.timer_func)
		timer.start(500)
		self.timers.append(timer)


	def timer_func(self):
		'''Fucntion handler for 1 sec timer'''
		
		# Connection Information

		if self.robot_connected == 0:	
			if 	self.connection_lost_indicator == 1:
				self.connection_lost_indicator =0
				self.label_4.setStyleSheet("background-color:red;")
			else:
				self.connection_lost_indicator =1
				self.label_4.setStyleSheet("background-color:none;")
		elif self.robot_connected == 1:
			self.label_4.setStyleSheet("background-color:green")
			self.label_4.setText("")
			self.robot_connected = 0


		self.gmap.moveRotationalMarker("swift", float(self.swift_lat), float(self.swift_lon), 30)




		

	def totalDistanceUpdate(self):

		if len(self.lat) > 1:
			total_distance = 0

			pos1 =LatLon23.LatLon(LatLon23.Latitude(self.lat[0]), LatLon23.Longitude(self.lon[0]))
			for x in range(1, len(self.lat)):
				pos2 = LatLon23.LatLon(LatLon23.Latitude(self.lat[x]), LatLon23.Longitude(self.lon[x]))
				total_distance = total_distance + pos1.distance(pos2)
				pos1 = pos2

			self.label_6.setText("Dist.: %.1f (m)" % (total_distance*1000))

			print (self.label_6.text())
		else:
			self.label_6.setText("")


	def setupMaps(self):
		self.markers_count = 0



		self.tableWidget.setColumnCount(3)

		w = self.widget
		h = QtGui.QVBoxLayout(w)
		l = QtGui.QFormLayout()
		h.addLayout(l)
		self.gmap = qgmap.QGoogleMap(w)

		self.gmap.setSizePolicy(
			QtGui.QSizePolicy.MinimumExpanding,
			QtGui.QSizePolicy.MinimumExpanding)	

		self.gmap.waitUntilReady()

		self.gmap.centerAt(41.143,-8.651)
		self.gmap.setZoom(13)

		h.addWidget(self.gmap)

		self.gmap.mapRightClicked.connect(self.onMapRClick)
		self.gmap.mapClicked.connect(self.onMapLClick)
		self.gmap.markerDoubleClicked.connect(self.onMarkerDClick)
		self.gmap.markerMoved.connect(self.markerDraged)

		#Table setup

		self.tableWidget.setColumnWidth(0,140)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setHorizontalHeaderLabels(["Latitude", "Longitude", "Time"])



		self.gmap.addRotationalMarker("swift",float(self.swift_lat), float(self.swift_lon), **dict(
			draggable=False,
			title = "swift",
			rotation = 10
			))




		# self.gmap.addRotationalMarker("swift", float(self.swift_lat), float(self.swift_lon), **dict(
		# icon="file:///home/pedro/Documents/SWIFT/Threading/swift.png",
		# draggable=False,
		# title = "swift" 
		# ))


		
	def onMapLClick(self,latitude, longitude) :
		print("LClick on ", latitude, longitude)

	def onMapRClick(self, latitude, longitude) :
		print("RClick on ", latitude, longitude)
		self.markers_count =  self.markers_count +1 
		self.markers_list.append( self.gmap.addMarker(str(self.markers_count), latitude, longitude, **dict(
		icon="http://chart.googleapis.com/chart?chst=d_map_pin_letter&chld="+str(self.markers_count)+"%7c5680FC%7c000000&.png%3f",
		draggable=True,
		title = str(self.markers_count) 
		)))

		self.tableWidget.setRowCount(self.markers_count)
		
		self.lat.append(latitude)
		self.lon.append(longitude)


		self.value_lat = QtGui.QTableWidgetItem(str(latitude))
		self.value_lon = QtGui.QTableWidgetItem(str(longitude))
		
		self.value_lat.setFlags(QtCore.Qt.ItemIsEnabled)
		self.value_lon.setFlags(QtCore.Qt.ItemIsEnabled)
		

		self.tableWidget.setItem(self.markers_count-1,0, self.value_lat )
		self.tableWidget.setItem(self.markers_count-1,1, self.value_lon )

		self.totalDistanceUpdate()

	def markerDraged(self, key, latitude, longitude):
		print(str(key) + " " + str(latitude) + " " + str(longitude))
		self.markers_list.append( self.gmap.addMarker(str(key), latitude, longitude, **dict(
		icon="http://chart.googleapis.com/chart?chst=d_map_pin_letter&chld="+str(key)+"%7c5680FC%7c000000&.png%3f",
		draggable=True,
		title = str(key) 
		)))

		self.lat[int(key)-1] = latitude
		self.lon[int(key)-1] = longitude

		self.value_lat = QtGui.QTableWidgetItem(str(latitude))
		self.value_lon = QtGui.QTableWidgetItem(str(longitude))
		
		self.value_lat.setFlags(QtCore.Qt.ItemIsEnabled)
		self.value_lon.setFlags(QtCore.Qt.ItemIsEnabled)
		

		self.tableWidget.setItem(int(key)-1,0, self.value_lat )
		self.tableWidget.setItem(int(key)-1,1, self.value_lon )

		self.totalDistanceUpdate()



	def onMarkerDClick(self,key, latitude, longitude) :
		''' On marker double click delete it'''

		print("DClick on ", key, latitude, longitude)
		#self.gmap.setMarkerOptions(key, draggable=True)
		self.markers_count = self.markers_count -1


		self.tableWidget.removeRow(self.lat.index(latitude))

		#clear all markers



		#delete all markers (create a function if used twice)
		for x in range(1, len(self.lat)+1):
			self.gmap.deleteMarker(x)


		#remove the marker double clicked

		self.lat.remove(latitude)
		self.lon.remove(longitude)
		#self.markers_list.remove(str(key))	

		x=0

		#draw all markers again ordered 
		for x in range(1, len(self.lat)+1):
			self.gmap.addMarker(str(x), self.lat[x-1], self.lon[x-1], **dict(icon="http://chart.googleapis.com/chart?chst=d_map_pin_letter&chld="+str(x)+"%7c5680FC%7c000000&.png%3f", draggable=True, title = str(x) ))


		self.reorderTableMarkers()

		self.totalDistanceUpdate()

	def reorderTableMarkers(self):
		self.tableWidget.setRowCount(len(self.lat))


	def closeEvent(self, event):

		choice = QtGui.QMessageBox.question(self, "Exit", "Are you sure?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print ("getting out")
			#message to kill all threads
			self.alive = 0
			#interface_queue.put("kill")
			sys.exit()
		else:
			pass



	def comunication_thread(self):

		sock_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		sock_recv.bind(("", UDP_RECV_PORT))
		sock_recv.settimeout(0.2)

		data_rcv = ""

		while self.alive == 1: 



#Receive part

			try:
				data_rcv, addr = sock_recv.recvfrom(1024)
				data_rcv = str(data_rcv)
			except socket.timeout:
				pass


			info = data_rcv.split(";")


			#heartbeat Swift
			try:

				index = info.index("swift_alive")
				self.robot_connected = 1

			except ValueError:
				print("swift not online")
				self.robot_connected = 0
				pass


			# posição swift
			try:
				index = info.index("s_pos")
				self.swift_lat = info[index +1].split("'")[0]
				self.swift_lon = info[index +2 ].split("'")[0]
				#print("moved")
				print("spos received "+ str(self.swift_lat)+ " "+ str(self.swift_lon))
			
			except ValueError:
				pass

			data_rcv  = ""



#Send Part
		
			# send mission coords

			

			if self.btn_send_clicked == 1:
				self.btn_send_clicked = 0

				message_to_send = ""
				#VELOCIDADE ;Mission;<numero de waypoints>;<mission_velocity>
				message_to_send = ";Mission;" + str(len(self.lat)) + ";" + str(0.0)

				for x in range(0, len(self.lat)):
					message_to_send = message_to_send + ";" + str(self.lat[x]) + ";" + str(self.lon[x])

				print(message_to_send)
				message_to_send = bytes(message_to_send, "utf-8")

				sock_send.sendto(message_to_send, (UDP_IP, UDP_SEND_PORT))


			if self.btn_start_clicked == 1:
				self.btn_start_clicked = 0

				message_to_send = ";STARTMISSION;"
				print(message_to_send)
				message_to_send = bytes(message_to_send, "utf-8")

				sock_send.sendto(message_to_send, (UDP_IP, UDP_SEND_PORT))



			if self.btn_stop_clicked == 1:
				self.btn_stop_clicked = 0

				message_to_send = ";STOPMISSION;"
				print(message_to_send)
				message_to_send = bytes(message_to_send, "utf-8")

				sock_send.sendto(message_to_send, (UDP_IP, UDP_SEND_PORT))



			time.sleep(0.1)

	def move_swift(self):
		#
		pass


	def launch_RosThreads(self):
		t1 = Thread(target = self.comunication_thread)
		t2 = Thread(target = self.ssh)
		t1.start()
		t2.start()


def main(argv):
	app = QtGui.QApplication(argv, True)
	wnd = MainWindow()
	wnd.show()
	app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))

# comunication thread	
	wnd.launch_RosThreads()


	sys.exit(app.exec_())


if __name__ == "__main__":
	main(sys.argv)

