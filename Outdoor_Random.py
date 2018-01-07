import pygatt
import time
from random import *
adapter = pygatt.GATTToolBackend()
adapter.start()
a=0
b=0
c=0
d=0
e=0

# wait to connect
while True:  
    try:
        device = adapter.connect('E8:77:6D:8B:09:96', timeout=1, address_type=pygatt.BLEAddressType.random)
        break
    except pygatt.exceptions.NotConnectedError:
        print('Waiting...')

while True:
	adapter.sendline('char-write-req 0x0011 ba20000a000800000e00e10005'+'{0:02x}'.format(a)+'{0:02x}'.format(b)+'{0:02x}'.format(c)+'{0:02x}'.format(d)+'{0:02x}'.format(e)+'')

	time.sleep(0.1)
	a =randint(1, 60)
	b =randint(1, 60)
	c =randint(1, 60)
	d =randint(1, 60)
	e =randint(1, 60)

adapter.stop()
