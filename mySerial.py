import serial
import serial.tools.list_ports
import time

coms = list(serial.tools.list_ports.comports())
com = coms[0][0]
print(com)

baud  = 19200;
timeout = 0.3;

ser = serial.Serial(
            port=com,
            baudrate=baud,
            timeout=timeout
        )

ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
# ser.stopbits = serial.STOPBITS_TWO
# ser.stopbits = serial.STOPBITS_ONE_POINT_FIVE
# ser.bytesize = serial.EIGHTBITS
ser.bytesize = serial.SEVENBITS

terminator = "CR"
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

    # if terminator == 'LN':
    #     self.terminator = '\n'
    # elif terminator == 'CR':
    #     self.terminator = '\r'
    # elif terminator == 'LNCR':
    #     self.terminator = '\n\r'
    # elif terminator == 'CRLN':
    #     self.terminator = '\n\r'
    # else:
    #     logging.error('Unknown terminator: ' + str(terminator))
    #     raise ValueError
    #
    # if terminator_space:
    #     self.terminator = ' ' + self.terminator

# def write(self, message: str) -> None:
#     ser = self.ser
#     try:
#         bmessage = (message + self.terminator).encode('utf-8')
#     except Exception:
#         logging.error('Can not create message to write')
#         self.close()
#         raise
#     ser.write(bmessage)
#     if self.logging_message:
#         logging.info(b'serial write: ' + bmessage)
#
#
# def write_readline(self, message: str) -> str:
#     ser = self.ser
#     try:
#         bmessage = (message + self.terminator).encode('utf-8')
#     except Exception:
#         logging.error('Can not create message to write')
#         self.close()
#         raise
#
#     # self.clear_input()
#     ser.write(bmessage)
#     if self.logging_message:
#         logging.info(b'serial write: ' + bmessage)
#
#     time.sleep(self.answer_time)
#     answer = ser.readline()
#     if self.logging_message:
#         logging.info(b'serial read: ' + answer)
#
#     return answer.decode('utf-8').rstrip('\n')