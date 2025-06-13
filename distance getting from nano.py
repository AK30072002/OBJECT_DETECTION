import smbus2
import time

bus = smbus2.SMBus(1)
address = 0x08

while True:
    try:
        data = bus.read_i2c_block_data(address, 0, 2)
        distance = data[0] | (data[1] << 8)
        print("Distance from Arduino:", distance, "cm")
    except OSError as e:
        print("I2C Error:", e)
    
    time.sleep(1)
