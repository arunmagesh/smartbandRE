import pygatt
import time
from random import *
adapter = pygatt.GATTToolBackend()
adapter.start()
a=0
# wait for someone to step on the scale
while True:  
    try:
        device = adapter.connect('E8:77:6D:8B:09:96', timeout=1, address_type=pygatt.BLEAddressType.random)
        break
    except pygatt.exceptions.NotConnectedError:
        print('Waiting...')

while True:
	adapter.sendline('char-write-req 0x0011 ba20008e00c00000060060008901fffe57006100')
	adapter.sendline('char-write-req 0x0011 63006b00200059006f0075002000500065007000')
	adapter.sendline('char-write-req 0x0011 6c0065000000000000000000000000000000000')
	adapter.sendline('char-write-req 0x0011 0000000000000000000000000000000000000000')
	adapter.sendline('char-write-req 0x0011 0000000000000000000000000000000000000000')
	adapter.sendline('char-write-req 0x0011 0000000000000000000000000000000000000000')
	adapter.sendline('char-write-req 0x0011 0000000000000000000000000000000000000000')
	adapter.sendline('char-write-req 0x0011 00000000000000000000')
	time.sleep(0.5)
	a = a + 1
	print('{0:02x}'.format(a))

adapter.stop()
