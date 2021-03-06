# DualBot
#-------------------------------------------------------------------------------Title: Network Test
#--Description: A qui se hace un testeo de una Ip especifica
#-------------------------------------------------------------------------------Libraries
import RPi.GPIO as GPIO
import time, os
#-------------------------------------------------------------------------------Other definitions
                                                                                #--El modo puede ser BCM o BOARD--#
#GPIO.setmode(GPIO.BCM)
                                                                                #--Pines de motores--#
#GPIO.setup(13, GPIO.OUT)
#GPIO.output(13, GPIO.LOW)
#GPIO.setup(23, GPIO.OUT)
#GPIO.output(23, GPIO.LOW)
#GPIO.setup(24, GPIO.OUT)
#GPIO.output(24, GPIO.LOW)
#GPIO.setup(25, GPIO.OUT)
#GPIO.output(25, GPIO.LOW)
                                                                                #--Pin de las luces--#
GPIO.setup(12, GPIO.OUT)
                                                                                #--Declaracion de pines para motores como PWM--#
#pwm1 = GPIO.PWM(13,100)
#pwm2 = GPIO.PWM(23,100)
#pwm3 = GPIO.PWM(24,100)
#pwm4 = GPIO.PWM(25,100)
                                                                                #--Declariion de variables como "ipAddress" o "response" a utlizar--#
#ipAddress = '192.168.1.77'
ipAddress = '172.17.92.30'
response = 0
#-------------------------------------------------------------------------------Definitions (DEF)
def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
                                                                                #--and then check the response..--#
    time.sleep(1)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
        #pwm1.start(0)
        #pwm2.start(0)
        #pwm3.start(0)
        #pwm4.start(0)
        #pwm1.stop()
        #pwm2.stop()
        #pwm3.stop()
        #pwm4.stop()
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(12, False)
        time.sleep(0.7)
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(12, False)
        time.sleep(0.7)
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(12, False)
                                                                                #--Retorna el valor de "pingstatus"--#
    return pingstatus
#-------------------------------------------------------------------------------The MAIN
if __name__ == "__main__":
    while True:
        try:
            pingstatus = check_ping(ipAddress)
            print pingstatus
        except KeyboardInterrupt:
            print "Algo fue mal :( "
            break
