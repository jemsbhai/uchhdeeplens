import serial
import json
import os
import random
##from twilio.rest import Client
import time
import sys
import pygame

imagename = "logo2.png"
pygame.init()
screen = pygame.display.set_mode((750,400))
pygame.mouse.set_visible(False)
image = pygame.image.load(imagename)
image = pygame.transform.scale(image, (750,400))
screen.blit(image, (0 , 0))
pygame.display.update()

### Your Account SID from twilio.com/console
##account_sid = "ACcdd8451104f384f1901a6888c1b0e074"
### Your Auth Token from twilio.com/console
##auth_token  = "2f874090954729c3166b210209986975"
##client = Client(account_sid, auth_token)

ser = serial.Serial('/dev/ttyACM0', 115200)



print ("connected to: " + ser.portstr)
count = 0
prevv = '#2525'
prev = '2525'

while True:
    line = ser.readline()
    print("read a line")
    print(line)

##    screen = pygame.display.set_mode((750,400))
##    pygame.mouse.set_visible(False)
##    image = pygame.image.load(imagename)
##    image = pygame.transform.scale(image, (750,400))
##    screen.blit(image, (0 , 0))
##    pygame.display.update()

    if int(line) <10:
        print ("user detected!")
        os.system('sudo google_speech "Hello. Please wait for image and record lookup"')
        os.system('sudo google_speech -l es "Hola. Por favor espera la foto"')
        
        os.system('sudo raspistill -rot 270 -o capture.jpg')
        ##user = os.popen('sudo python simplepirekognizer.py capture.jpg').read()
        print ('\n user input detected!!\n')
        print ('\n taking photo of user \n')
        os.system('sudo python simplepirekognizer.py capture.jpg > result.txt')
        with open('result.txt','r') as f:
            for line in f:
                for word in line.split():
                   print(word)
                   user = word
        
        print (user)
        if user == 'none':
            os.system('sudo google_speech "Hello. Please proceed straight to the main reception desk."')
            os.system('sudo google_speech -l es "Hola. Por favor vaya directamente a la recepcion."')
            pygame.quit()
            os.system('sudo python showpic.py bluearrowup.png 5')

        if user == 'muntaser':
            os.system('sudo google_speech "Hello mister say ed. Please go to the main auditorium"')
            pygame.quit()
            ##os.system('sudo python showpic.py room1.JPG 5')
            os.system('sudo python showpic.py right.png 7')

        if user == 'chris':
            ##os.system('sudo google_speech "Hello mister chris. Please go to the auditorium"')
            os.system('sudo google_speech -l es "Hola senor Juan. Por favor ve al auditorio"')
            pygame.quit()
            ##os.system('sudo python showpic.py room2.JPG 5')
            os.system('sudo python showpic.py left.png 7')

        if user == 'woodle':
            os.system('sudo google_speech "Hello mister wood. Please go to room two seventy six"')
            pygame.quit()
            os.system('sudo python showpic.py room1.JPG 5')
            os.system('sudo python showpic.py bluearrowleft.png 7')

        if user == 'andrew':
            os.system('sudo google_speech "Hello mister andrew. Please go to room two twenty nine"')
            pygame.quit()
            os.system('sudo python showpic.py room2.JPG 5')
            os.system('sudo python showpic.py bluearrowright.png 7')



        ser.flushInput()
        ser.flushOutput()
        time.sleep(1)
        
time.sleep(1)
pygame.quit()


