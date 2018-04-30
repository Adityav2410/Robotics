'''
**********************************************************************
* Filename    : views
* Description : views for server
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''

from driver import camera, stream
import picar
import numpy as np
import cv2
import cv2.cv as cv
from datetime import datetime
from PIL import Image
import os
import time

#picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
 
#print stream.start()

class Camera:

    def __init__(self, debug = False):
        self.cam = camera.Camera(debug=debug, db=db_file)
        self.cam.ready()
        self.horizAngle = 0
        self.vertAngle = 0
        self.dirpath = './frameCaptured'

    def __del__(self):
        del self.cam
                 
    def turn_left(self, angle=20):
        self.cam.turn_left(angle)
        self.horizAngle -= angle
        
    def turn_right(self, angle=20):
        self.cam.turn_right(angle)
        self.horizAngle += angle
 
    def turn_down(self, angle=20):
        self.cam.turn_down(angle)
        self.vertAngle -= angle
 
    def turn_up(self, angle=20):
        self.cam.turn_up(angle)
        self.vertAngle += angle
    
    def reset(self):
        self.cam.ready()
        self.horizAngle = 0
        self.vertAngle = 0
      
    def captureFrame(self):
        img = cv2.VideoCapture(-1)
        _, bgr_image = img.read()
        #rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        #img.release()

        return (bgr_image)
        
    def saveFrame(self, dirpath=None, filename=None):
        if not filename:
            filename = datetime.now().strftime("%Y%m%d-%H-%M%S")
        if not dirpath:
            dirpath = self.dirpath

        frame = self.captureFrame()
        Image.fromarray(frame).save(os.path.join(dirpath, filename)+'.jpg' )
#/home/pi/SunFounder_PiCar-V/remote_control/remote_control
