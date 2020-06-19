# Module for STP-DRV-4850 serial communication

import time
import serial

class Serial4850:
    step_angle_per_number =  
    def __init__(self, port_path):

        self.port_path = port_path

        self.ser = serial.Serial(port = port_path, baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS)

        self.ser.isOpen()

    def rotate(self, degrees):

        self.ser.write(("FL" + degrees + "\r").encode('ascii'))

stp = Serial4850('COM4')

"""
print('Enter your commands below.\r\nInsert "exit" to leave the application.')

inputT=1
while 1 :
    # get keyboard input
    inputT = input(">> ")

    if inputT == 'exit':
        ser.close()
        exit()
    else:

        ser.write((inputT + "\r").encode('ascii'))
        out = ''

        time.sleep(1)
        while ser.inWaiting() > 0:
            out += str(ser.read(1))

        if out != '':
            print(">>" + out)
"""