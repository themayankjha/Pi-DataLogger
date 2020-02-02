import matplotlib.pyplot as plot
import time
import shutil
import os
content_list = []
def file_read(fname):
        with open(fname) as f:    
                for line in f:
                        content_list.append(line.strip('\n'))
                print(content_list)
                

file_read('sensor1.txt') 
print ("Original list is : " + str(content_list)) 
for i in range(0, len(content_list)): 
    content_list[i] = float(content_list[i])
print ("Modified list is : " + str(content_list))
plot.hist(content_list, bins=[9.00,9.15,9.30,9.45,10.00,10.15,10.30,10.45,11.00,11.15,11.30,11.45,12.00,
                  12.15,12.30,12.45,13.00,13.15,13.30,13.45,14.00,14.15,14.30,14.45,15.00,15.15,15.30,15.45,16.00,16.15,16.30,16.45,17.00,
                  17.15,17.30,17.45,18.00,18.15,18.30,18.45,19.00,19.15,19.30,19.45,20.00,20.15,20.30,20.45,21.00,21.15,21.30,21.45,22.00],align='left', histtype='bar', rwidth=0.5, color='green')




plot.xlabel("Time")
plot.ylabel("Frequency")
plot.title("NUMBER OF CUSTOMERS")
plot.savefig('sensordata1.png')
os.replace("sensordata1.png", time.strftime("%Y%m%d.png"))
os.replace(time.strftime("%Y%m%d.png"), "sensor1/"+time.strftime("%Y%m%d.png"))


