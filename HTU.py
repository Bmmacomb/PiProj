import time
import smbus


def Humid():
   DEV_ADDR = 0x40

   i2c = smbus.SMBus(1)

   CMD_READ_TEMP_HOLD = 0xe3
   CMD_READ_HUM_HOLD = 0xe5
   CMD_READ_TEMP_NOHOLD = 0xf3
   CMD_READ_HUM_NOHOLD = 0xf5
   CMD_WRITE_USER_REG = 0xe6
   CMD_READ_USER_REG = 0xe7
   CMD_SOFT_RESET= 0xfe

   i2c.write_byte(DEV_ADDR, CMD_SOFT_RESET)
   time.sleep(.1)
   i2c.write_byte(DEV_ADDR, CMD_READ_HUM_NOHOLD)
   time.sleep(.06)
   msb = i2c.read_byte(DEV_ADDR)
   #print bin(msb)
   ans = msb
   #print ans
   #this accounts for the unretreivable LSBs 
   ans = ans << 8
   #print ans
   #create a float for the result
   hum = float (ans)
   #the following is the formula for retrieving the humidity reading per datasheet
   hum = (hum / (65536))
   hum = hum * 125
   #print hum
   hum = hum - 6
#   print hum
   return hum
