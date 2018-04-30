import time
import numpy as np

from picar import back_wheels, front_wheels
import picar
import math

picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"

class Movement:

   
    def __init__(self):
        self.fw = front_wheels.Front_Wheels(debug=False, db=db_file)
        self.bw = back_wheels.Back_Wheels(debug=False, db=db_file)
        self.bw.ready()
        self.fw.ready()
        self.turnStraight()
        self.speed = 60
        self.bw.speed = 0 #self.speed
        self.fw_status = 0
        self.bw_status = 0
    	self.fw.turning_max = 40

        ###### Parameters to translate robot speed 0-100 to absolute speed in cm/s
        self.ref_speed = 20
        self.ref_abs_speed = 3.6667
        self.slope_speed = 0.6885
        self.abs_speed = self.getAbsoluteSpeed()
        
        ###### Physical parameters of the car ##########################
        self.L = 0.145   # The distance between front and rear wheels(in m).
 
    
    def __del__(self):
    	del self.fw
    	del self.bw
    	print("Deleted movement object")
    
    
    ####### Functions to control speed of car #######################
    def setSpeed(self,speed):
        self.speed = speed
        self.abs_speed = self.getAbsoluteSpeed()
        #self.bw.speed = speed
    
    def setAbsoluteSpeed(self, abs_speed):
        abs_speed *= 100  ## convert m/s to cm/s
    	self.speed =  int( (abs_speed- self.ref_abs_speed)/self.slope_speed + (self.ref_speed) )
        self.abs_speed = self.getAbsoluteSpeed()
    
    def getAbsoluteSpeed(self):
        abs_speed = self.ref_abs_speed + (self.speed - self.ref_speed)*self.slope_speed
        return round(abs_speed/100.0, 4)    
    
    ################# Functions related to steering front wheel #############
    def turnStraight(self, angle=0):
        self.fw.turn_straight()
    
    def turnLeft(self, angle=35):
        if angle is None:
            angle = 20
        else:
            angle = min(angle, self.fw.turning_max)
    
        self.fw.wheel.write(self.fw._straight_angle - angle)
    
    def turnRight(self, angle=35):
        if angle is None:
            angle = 20
        else:
       	    angle = min(angle, self.fw.turning_max)
        self.fw.wheel.write(self.fw._straight_angle + angle)
    
    def getSteerAngle(self, radius):
        #### tan(theta) = L/radius
        return int( math.degrees(math.atan( self.L/float(radius) )) )
    
    def turnLeftForRadius(self, radius):
        angle = self.getSteerAngle(radius)
        self.turnLeft(angle)
    
    def turnRightForRadius(self, radius):
        angle = self.getSteerAngle(radius)
        #print("Turning right for radius: ", radius, "\t Turn angle: ",angle  )
        self.turnRight(angle)
    
    
    ################# Functions to control the rear/back wheel movement ########3
    
    def moveForward(self, t=0):
    	#print("Move forward for time: ", t)
    	self.bw.speed = self.speed
        self.bw.forward()
        self.bw_status = 1
        if t>0:
            time.sleep(t)
            self.bw.speed = 0
            self.bw_status = 0
    def moveBackward(self, t=0):
    	self.bw.speed = self.speed
        self.bw.backward()
        self.bw_status = -1
        if t>0: 
            time.sleep(t)
            self.bw.speed = 0
            self.bw_status = 0
    
    def pause(self, t=2):
        self.bw.speed = 0
        temp_status = self.bw_status 
        self.bw_status = 0
        time.sleep(t)
        self.bw.speed = self.speed
        self.bw_status = temp_status
    
    def stop(self):
        self.bw_status = 0
        #self.bw.stop()
        self.bw.speed = 0
    
    def moveForwardDist(self, dist):
        moveTime = round(dist/self.abs_speed, 3)
        self.moveForward(moveTime)
    
    def moveBackwardDist(self, dist):
    	moveTime = round(dist/self.abs_speed, 3)
        self.moveBackward(moveTime)
    
    
    ################## Helper function ##########################################
    
    def turnRightNinty(self):
        self.turnRight(35)
        self.moveForwardDist(0.25)
        self.turnLeft(35)
        self.moveBackwardDist(0.33)
        self.turnStraight()
    
    def turnRightFortyFive(self):
        self.turnRight()
        self.moveForward(1.25)
        self.turnStraight()
        self.moveBackward(1)
    
    def turnLeftFortyFive(self):
        self.turnLeft(35)
        self.moveForwardDist(0.3)
        self.turnStraight()
        self.moveBackward(0.2)
    
    def turnLeftNinty(self):
        self.turnLeft(35)
        self.moveForwardDist(0.25)
        self.turnRight()
        self.moveBackwardDist(0.35)
        self.turnStraight()
    
