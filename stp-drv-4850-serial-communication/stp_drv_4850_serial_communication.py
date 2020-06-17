import time
import serial

ser = serial.Serial(
    port='COM4',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

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