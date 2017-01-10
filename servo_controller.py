import time
from  './Adafruit-Raspberry-Pi-Python-Code/Adafruit_PWM_Servo_Driver' import Adafruit_I2C
from  './Adafruit-Raspberry-Pi-Python-Code/Adafruit_PWM_Servo_Driver' import Adafruit_PWM_Servo_Driver

# ===========================================================================
# Coffee Maker Bot Script
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
                                                            #  1,1           Top

# servoMin = 150  # Min pulse length out of 4096
# servoMax = 600  # Max pulse length out of 4096
# 
# def setServoPulse(channel, pulse):
#   pulseLength = 1000000                   # 1,000,000 us per second
#   pulseLength /= 60                       # 60 Hz
#   print "%d us per period" % pulseLength
#   pulseLength /= 4096                     # 12 bits of resolution
#   print "%d us per bit" % pulseLength
#   pulse *= 1000
#   pulse /= pulseLength
#   pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
while (True):
  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, servoMin)
  time.sleep(1)
  pwm.setPWM(0, 0, servoMax)
  time.sleep(1)