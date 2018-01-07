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
	adapter.sendline('char-write-req 0x0011 ba20000c001e00010200200007'+'{0:02x}'.format(a)+'{0:02x}'.format(b)+'{0:02x}'.format(c)+'{0:02x}'.format(d)+'{0:02x}'.format(e)+'0000')
	time.sleep(0.5)
	# print('a'+str(a)+'b'+str(b)+'c'+str(c)+' ') 
	a =randint(1, 60)
	b =randint(1, 60)
	c =randint(1, 60)
	d =randint(1, 60)
	e =randint(1, 60)
adapter.stop()


# 2 -- sec 3 - min 4 - hour 5-- date 6 -- month 7 -- year
