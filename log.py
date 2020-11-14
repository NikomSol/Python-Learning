import logging
import sys

def excepthook(*args):
  logging.getLogger().error('Uncaught exception:', exc_info=args)
sys.excepthook = excepthook


logging.basicConfig(filename="log.txt", level=logging.INFO, filemode='w')
"DEBUG, INFO, WARNING, ERROR, CRITICAL"
print('Hell0')
logging.debug("This is a debug message")
logging.info(b'aa' + b"Informational message\n")
x = 'dsd'
logging.error("An error has happened! " + str(x))

try:
    print(1/0)
except:
    logging.error('11')
finally:
    print('b')

assert 1==0
print('eee')