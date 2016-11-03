'I.T.S
'Image To Speech
'This process takes an image, which is then converted into text and then finally converted into audio 
'Meant to be used on a raspberry Pi 3
'Developed by Kamran Tayyab and Johnny Hoang
RPi.GPIO as GPIO
import time
import subprocess
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

filen = "out.txt"
mouse = True

while True:
        subprocess.call("espeak 'Ready to take Picture'",shell=True)
	input_state = GPIO.input(18)
	if input_state == False:
		subprocess.call("espeak 'Taking Picture'", shell=True)
		subprocess.call("raspistill -md 4 -sh 80 -vf -hf -ev 10 -ex auto -o Image.jpg", shell=True)
		time.sleep(5)
		subprocess.call("espeak 'Converting Picture'", shell=True)
		subprocess.call("tesseract Image.jpg out", shell=True)
		time.sleep(10)
		subprocess.call("espeak 'Checking if file exist'", shell=True)
                while os.path.exists(filen) and mouse:
                        FileSize = os.path.getsize(filen)
                        if FileSize > 3:
                                print("Converting into speech")
                                subprocess.call("espeak -f out.txt", shell=True)
                                time.sleep(1)
                                subprocess.call("python Script.py &")
                                exit()
                        else:
                                print("File does not have text inside of it")
                                subprocess.call("espeak 'File cannot be read, please take a better picute'", shell=True)
                                mouse = False
                                subprocess.call("python Script.py &")
                                exit()

