import random
import multiprocessing
import bit
import time
print ("Seeking Puzzle")


# startTime = time.time()
while True:
    startTime = time.time()# это начало цикла закоментируешь, а выше разкоментируешь, будет показывать общее время)
    x = random.randint(2**65, 2**66)
    y = bit.Key.from_int(x).address
    print ("\r" + y + ':' + str(x), end=" ")
    endTime = time.time()
    totalTime = endTime - startTime
    print ("\r" + y + ':' + str(x) + ' : ' + str(totalTime), end=" ",flush=True)
    if y == '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so':
        f = open("Found.txt","a")
        f.write (hex(x)[2:])
        f.close()
        print(hex(x)[2:])
        break
   
