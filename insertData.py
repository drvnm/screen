import csv
import random
import time
fieldnames = ['ID', 'MSG', 'HOUR']
ids = [0x1004000, 0x1004001, 0x4002]
index = 0
with open('dataFiles/data.csv', 'w') as w:
    writer = csv.DictWriter(w, fieldnames=fieldnames)
    writer.writeheader()

while True:

    if index >= 24:
        index = 0
    with open('dataFiles/data.csv', 'a') as i:
        writer = csv.DictWriter(i, fieldnames=fieldnames)

        id = random.choice(ids)
        msg = str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) + '/' + str(random.randint(0,255)) 
        hour = index

        info = {
            'ID': id,
            'MSG': msg,
            'HOUR': hour
        }
        index +=1
        print(id,msg,hour)
        writer.writerow(info)
    time.sleep(0.3)
