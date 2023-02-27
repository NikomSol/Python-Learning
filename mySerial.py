import serial
import serial.tools.list_ports
import time

# coms = list(serial.tools.list_ports.comports())
# com = coms[0][0]
com = 'COM4'
print(com)

baud  = 19200;
timeout = 0.5;

ser = serial.Serial(
            port=com,
            baudrate=baud,
            timeout=timeout
        )

ser.parity = serial.PARITY_NONE
# ser.parity = serial.PARITY_EVEN
# ser.parity = serial.PARITY_ODD
ser.stopbits = serial.STOPBITS_ONE
# ser.stopbits = serial.STOPBITS_TWO
# ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE
ser.bytesize = serial.EIGHTBITS
# ser.bytesize = serial.SEVENBITS
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False

terminator = "CRLN"
if terminator == 'LN':
    terminator = '\n'
elif terminator == 'CR':
    terminator = '\r'
elif terminator == 'LNCR':
    terminator = '\n\r'
elif terminator == 'CRLN':
    terminator = '\n\r'

message = "*IDN?"

bmessage = (message + terminator).encode('utf-8')
ser.write(bmessage)

time.sleep(timeout)
answer = ser.readline()
print("answer = ", answer.decode('utf-8')) #.rstrip('\n')

print(ser.isOpen())
ser.close()
