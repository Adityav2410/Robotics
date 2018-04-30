import time
import numpy as np

from picar import back_wheels, front_wheels
import picar
from movement import Movement
from cameraUtils import Camera
import time
picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"


def speedAnalysis():
    speedList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    timeList  = [30, 30, 20, 20, 10, 10, 5, 5, 4, 4]
    mov = Movement()
    for speed, time in zip(speedList, timeList):
	print("Speed: ", speed, "\t Time: ", time,"\n")
	mov.setSpeed(speed)
	mov.moveForward(time)
        mov.pause(15)
    mov.stop()
    del mov

        
def experiment1():
    mov = Movement()
    
    mov.setAbsoluteSpeed(0.35)

    mov.turnRightForRadius(0.25)
    mov.moveForward(30)
    mov.pause(30)    
    
    
    mov.turnRightForRadius(0.35)
    mov.moveForward(30)
    mov.pause(30)

    mov.turnRightForRadius(0.45)
    mov.moveForward(30)
    mov.pause(30)


    mov.turnRightForRadius(0.55)
    mov.moveForward(30)
    mov.pause(30)
     #mov.moveForwardDist(3)
#    mov.moveBackwardDist(2)
#    mov.stop()
    #mov.turnLeft(20)
#    time.sleep(2)
#    mov.turnLeft(40)
#    time.sleep(2)
#    mov.turnRight(20)
#    time.sleep(2)
    #mov.turnStraight()
    mov.stop()
    #mov.stop()
    del mov
#    mov.moveForward(2)
#    mov.turnStraight()
#    mov.turnRight()
#    stop(bw)



class Traverse:

    def __init__(self):
        coordList = []
        self.currLocation = [0, 0, 90]



        self.nSteps = len(coordList)
        self.mov = Movement()
        self.rad = 180/3.14

    def startTraversal(self):
        # Origin
    
        # Stop No. 1
        self.mov.moveForwardDist(1)
        self.mov.pause(5)

        # Stop No. 2
        self.mov.turnLeftNinty()
        self.mov.moveForwardDist(1)
        self.mov.pause(5)

        # Stop No 3
        self.mov.turnRightNinty()
        self.mov.moveForwardDist(1)
        self.mov.pause(5)

        # Stop No 4
        self.mov.turnLeftNinty()
        self.mov.moveForwardDist(1)
        self.mov.turnLeftNinty()
        self.mov.turnLeftNinty()
        self.mov.pause(5)

        # Stop No 5
        self.mov.turnRightNinty()
        self.mov.moveForwardDist(1)
        self.mov.turnLeftNinty()
        self.mov.moveForwardDist(1)
        self.mov.turnLeftFortyFive()
        self.mov.pause(5)

        # Stop No 6
        self.mov.turnRightNinty()
        self.mov.turnRightFortyFive()
        self.mov.moveForwardDist(1)
        self.mov.turnLeftNinty()
        self.mov.moveForwardDist(1)
        self.mov.turnLeftNinty()
        self.mov.pause(20)


    def calibration(self):
        for i in range(10):
            self.mov.turnRightNinty()
            self.mov.pause(8)



def customMain(fw, bw):
    print ("Custom main function called: Yippie")
    #trav = Traverse()
    #trav.calibration()
    #trav.startTraversal()



def captureFrameExperiment():
    cam = Camera()
    
    cam.saveFrame(filename='dist_1.5m')
    #cam.saveFrame(filename='dist_1.5m')
    print("Frame 2 captured")
    #time.sleep(9)
    #cam.saveFrame(filename='dist_1m')
    #print("Frame 2 captured")
    #time.sleep(9)
    #cam.saveFrame(filename='dist_0.5m')
    #print("Frame 3 captured")


if __name__ == '__main__':
    #experiment1()
    captureFrameExperiment()
    #speedAnalysis()
