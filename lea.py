# Lea alternate by Naoned Makers
# Control Lea with Adafruit Capacitive touch
# and 16 Channels PWM/Servo hats

#!/usr/bin/python

import sys
import time

# --- CONFIGURATION CAPACITATIVE TOUCH ---

import Adafruit_MPR121.MPR121 as MPR121

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

# === FIN ===

# --- CONFIGURATION SERVO HAT ---

from Adafruit_PWM_Servo_Driver.Adafruit_PWM_Servo_Driver import PWM # Servo Hat

# Initialise the PWM device using the default address
pwm = PWM(0x40)

# BRAS DROIT - TOWER PRO MG 92B 50Hz
CHANNEL_RIGHT_ARM = 0
SERVO_MIN_RIGHT_ARM = 160  # Min pulse
SERVO_MAX_RIGHT_ARM = 350  # Max pulse

# TETE - TOWER PRO MG 92B 50Hz
CHANNEL_HEAD = 1
SERVO_MIN_HEAD = 160  # Min pulse
SERVO_MID_HEAD = 330  # Middle pulse
SERVO_MAX_HEAD = 500  # Max pulse

# BRAS GAUCHE - TOWER PRO MG 92B 50Hz
CHANNEL_LEFT_ARM = 2
SERVO_MIN_LEFT_ARM = 350  # Min pulse
SERVO_MAX_LEFT_ARM = 160  # Max pulse

pwm.setPWMFreq(50) # Set frequency to 50Hz

# Initialise les servos
pwm.setPWM(CHANNEL_RIGHT_ARM, 0, SERVO_MIN_RIGHT_ARM)
pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MIN_LEFT_ARM)
pwm.setPWM(CHANNEL_HEAD, 0, SERVO_MID_HEAD)

def rightArm(sleep = 1):
  pwm.setPWM(CHANNEL_RIGHT_ARM, 0, SERVO_MAX_RIGHT_ARM)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_RIGHT_ARM, 0, SERVO_MIN_RIGHT_ARM)
  time.sleep(sleep)

def leftArm(sleep = 1):
  pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MAX_LEFT_ARM)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MIN_LEFT_ARM)
  time.sleep(sleep)

def head(sleep = 1):
  pwm.setPWM(CHANNEL_HEAD, 0, SERVO_MAX_HEAD)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_HEAD, 0, SERVO_MID_HEAD)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_HEAD, 0, SERVO_MIN_HEAD)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_HEAD, 0, SERVO_MID_HEAD)
  time.sleep(sleep)

# === FIN ===

# --- INTERACTIONS ---

# Check if a pin is touched.
print('Lea Alternate with Capacitive Touch Sensor & 16 Channels PWM/Servo Hat')
print('Press Ctrl-C to quit.')

last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    if cap.is_touched(1):
       print('Pin 1 : Rien ne se passe')

    if cap.is_touched(4):
    	print('Pin 4 : Leve le bras droit')
	rightArm()

    if cap.is_touched(5):
    	print('Pin 5 : tourne la tete')
	head()

    if cap.is_touched(6):
    	print('Pin 6 : Leve le bras gauche')
	leftArm()

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    #time.sleep(0.1)

# === FIN ===


