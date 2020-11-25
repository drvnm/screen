import csv
import pandas as pd
import can
import time
import datetime
fieldnames = ['ID', 'MSG', 'HOUR']
ids = [16778240, 0x1004001, 0x4002]

index = 1
with open('dataFiles/dataCAN.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=fieldnames)
    writer.writeheader()
bus = can.interface.Bus(channel='can0')
while 1:
    msg = bus.recv(1)
    
    with open('dataFiles/dataCAN.csv', 'a') as i:
        writer = csv.DictWriter(i, fieldnames=fieldnames)
            
        id = 3
        msg = str(msg.data[0]) + '/' + str(msg.data[1]) + '/' + str(msg.data[2]) + '/' + str(msg.data[3]) + '/' + str(msg.data[4]) + '/' + str(msg.data[5]) + '/' + str(msg.data[6]) + '/' + str(msg.data[7]) 
        hour = datetime.datetime.now().hour

        info = {
            'ID': id,
            'MSG': msg,
            'HOUR': hour
        }
        index +=1
        print(id,msg,hour)
        writer.writerow(info)
    
