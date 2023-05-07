import serial
import time
import io

ser = serial.Serial('/dev/cu.usbmodem1302', baudrate=115200, timeout=0)

counter = 0
#read the input from the serial port
while True:                             # runs this loop forever
    time.sleep(.001)                    # delay of 1ms
    val = ser.readline()                # read complete line from serial output
    while not '\\n'in str(val):         # check if full data is received. 
        # This loop is entered only if serial read value doesn't contain \n
        # which indicates end of a sentence. 
        # str(val) - val is byte where string operation to check `\\n` 
        # can't be performed
        time.sleep(.001)                # delay of 1ms 
        temp = ser.read()           # check for serial output.
        counter+=1
        if not not temp.decode():       # if temp is not empty.
            val = (val.decode()+temp.decode()).encode()
            # requrired to decode, sum, then encode because
            # long values might require multiple passes
    val = val.decode()                  # decoding from bytes
    val = val.strip()                   # stripping leading and trailing spaces.
    
    print(val)
    msg = str(counter)+"\n"
    ser.write(msg.encode('utf_8'));
   
#if button A is pressed, mimick the keyboard "SPACE" on the computer
