import time
import random 
import sys


print(sys.argv)
start_time = int(time.time())
itime = start_time 
run_time = int(sys.argv[1]) # gets arguments from terminal, has to input after name 

file_name = 'data.csv' #saves file 
if(len(sys.argv) > 2): 
    file_name = sys.argv[2] 
    
print(file_name)  
file = open(file_name, 'w')  
writer = csv.writer(file)
meta_data = ["Time", "Data"]
writer.write

while itime < (start_time + run_time): 
    itime = int(time.time()) # gives u the massive amount of seconds, timestamp 
    value = random.random() #the same as grapping data from a server
    print(itime, value)
    time.sleep(1)



