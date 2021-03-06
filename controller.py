import RPi.GPIO as GPIO
import time
from subprocess import call
import subprocess
from viz import *

GPIO.setmode(GPIO.BCM)

class ButtonRecorder: 
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	def getInputState(self):
		input_state = GPIO.input(self.pin)
		return input_state

	def start(self): 
		print("Say something! (:")
		subprocess.Popen(["python","/home/pi/Desktop/waves/killer.py",str(self.pin)])
		print("Recording now")
		call(["arecord","/home/pi/Desktop/waves/audio.mp3", "-D", "sysdefault:CARD=1"])
		print("Recording stopped")
		createViz(self.pin)  
		print("Viz Created")


rec23 = ButtonRecorder(23)
s23 = rec23.getInputState()

rec24 = ButtonRecorder(24)
s24 = rec24.getInputState()

rec25 = ButtonRecorder(25)
s25 = rec25.getInputState()

rec8 = ButtonRecorder(8)
s8 = rec8.getInputState()

while True:
	if (rec23.getInputState() == False):
		rec23.start()
	elif (rec24.getInputState() == False):
		rec24.start()
	elif (rec25.getInputState() == False):
		rec25.start()
	elif (rec8.getInputState() == False):
		rec8.start()
