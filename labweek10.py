import RPi.GPIO as GPIO
import datetime
import time
import sys
import csv

channel = 6
counts = 0

if len(sys.argv) > 1:
 run_time = int(sys.argv[1])
 if len(sys.argv) > 2:
  count_time = int(sys.argv[2])
  if len(sys.argv) > 3:
   output_file_name = sys.argv[3]
   output_file_name = output_file_name + ".csv"
 
 def my_callback(channel):
  global counts
  #print('\falling at ' + str(datetime.datetime.now()))
  counts = counts + 1
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, callback=my_callback, bouncetime=10)
GPIO.setwarnings(False)
 

f = open(output_file_name,"w")
meta_data = ["CPM","Time"]

f = open(output_file_name,"w",newline='')
writer = csv.writer(f)
writer.writerow(meta_data)

startTime=int(time.time())
iTime=startTime
list_of_times = []
originalStart = int(time.time())


while iTime <= (startTime + run_time):
 time.sleep(count_time)
 print("Counts in the last count_time: " + str(counts))
 data = [str(counts),str(time.time())]
 writer.writerow(data)
 iTime = int(time.time())
 counts = 0
 
f.close()
