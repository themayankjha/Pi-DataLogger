#Libraries
import RPi.GPIO as GPIO
import time
import datetime
#GlobalVariables
passedtime=0
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 2
GPIO_ECHO = 3
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
def log():
    print("Sensor 1 has Sucessfully logged")
    currentDT = datetime.datetime.now()
    print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
    passedtime=0
    f=open("sensor1.txt", "a+") 
    f.write(currentDT.strftime("%H.%M\n")) 
    f.close 
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance from sensor 1 = %.1f cm" % dist)
            while dist < 35:
                dist=distance()
                time.sleep(1)
                passedtime = passedtime+1
                if dist > 35 :
                    passedtime=0
                    break;
                if passedtime==10 :
                    log()
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
