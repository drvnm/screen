import os

pip = ['pillow', 'queuelib', 'threaded', 'python-can', 'queue', 'tkinter']
apt = ['python3-tk']

for pack in pip:
    try:
        os.system('pip3 install ' + pack)
    except:pass
for pack in apt:
    try:
        os.system('sudo apt-get install ' + pack)
    except:pass
    