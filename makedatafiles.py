import random

datasize = 10

for i in range(0,7) :
   filename = "data" + str(datasize) + ".txt"
   file = open(filename, "w")

   for n in range(0,datasize) :
       newnum = random.randint(0, 100000000)
       file.write(str(newnum)+"\n")

   file.close()
   datasize *= 10

