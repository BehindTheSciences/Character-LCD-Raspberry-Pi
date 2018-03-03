#!/usr/bin/python
#--------------------------------------
#  16x2 LCD Rasbperry Pi Test Script
#
# Author : BehindTheSciences
# Date   : 14/02/2017
#
# https://behindthesciences.com
#
#--------------------------------------

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import time
from BTSLCDPi import BTSLCD

LCD_LINE_1 = 1
LCD_LINE_2 = 2
# GPIO to LCD mapping
LCD_RS            = 14
LCD_EN            = 18
LCD_D4            = 24
LCD_D5            = 23
LCD_D6            = 8
LCD_D7            = 25

#Create LCD class
LCD = BTSLCD(GPIO,LCD_EN,LCD_RS,LCD_D4,LCD_D5,LCD_D6,LCD_D7)
 
def main():
  
 
  # Initialise display
  LCD.lcd_init()
 
  while True:
 
    # Send some test
    LCD.lcd_string("Rasbperry Pi",LCD_LINE_1)
    LCD.lcd_string("16x2 LCD Test",LCD_LINE_2)
 
    time.sleep(3) # 3 second delay
 
    # Send some text
    LCD.lcd_string("1234567890123456",LCD_LINE_1)
    LCD.lcd_string("abcdefghijklmnop",LCD_LINE_2)
 
    time.sleep(3) # 3 second delay
 
    # Send some text
    LCD.lcd_string("BehindTheScience",LCD_LINE_1)
    LCD.lcd_string("s.com",LCD_LINE_2)
 
    time.sleep(3)
 
    LCD.lcd_string("1234567890123456",LCD_LINE_1)
    LCD.lcd_string("ABCDEFGHIJKLMNOP",LCD_LINE_2)
 
    time.sleep(3) # 3 second delay
 
    time.sleep(3)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
