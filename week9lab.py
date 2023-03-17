import RPi.GPIO as GPIO
import datetime
import time

channel = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

f = open("data5.csv","w")
meta_data = ["CPM","Time Tags"]
import csv
f = open("data5.csv","w",newline='')
writer = csv.writer(f)
writer.writerow(meta_data)

startTime=int(time.time())
iTime=startTime
count = 0
list_of_times = []
originalStart = int(time.time())

while iTime < (originalStart + 140):
 temp = GPIO.wait_for_edge(channel, GPIO.FALLING, timeout = 1000)
 if temp is None:
  print("Timeout")
 else:
  count = count + 1
 list_of_times.append(str(datetime.datetime.now()))
 iTime = int(time.time())
 if iTime > (startTime + 60):
  data = [str(count),str(list_of_times)]
  writer.writerow(data)
  print("Counts in the last minute: " + str(count))
  count = 0
  list_of_times = []
  startTime = int(time.time())
 
print("Total Counts:" + str(count))
f.close()