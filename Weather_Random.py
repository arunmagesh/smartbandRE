import pygatt
import time
from random import *
adapter = pygatt.GATTToolBackend()
adapter.start()
a=0
b=0
c=0

# wait for someone to step on the scale
while True:  
    try:
        device = adapter.connect('E8:77:6D:8B:09:96', timeout=1, address_type=pygatt.BLEAddressType.random)
        break
    except pygatt.exceptions.NotConnectedError:
        print('Waiting...')

while True:
	adapter.sendline('char-write-req 0x0011 ba20000b004c00050300300006'+'{0:02x}'.format(a)+'{0:02x}'.format(b)+'{0:02x}'.format(c)+'000000')
	time.sleep(0.5)
	print('a'+str(a)+'b'+str(b)+'c'+str(c)+' ') 
	a =randint(1, 99)
	b =randint(1, 99)
	c =randint(1, 5)
adapter.stop()



