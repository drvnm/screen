import os

pip = ['pillow', 'queuelib', 'threaded', 'PySimpleGUI', 'python-can']
apt = ['python3-tk']

for pack in pip:
    os.system('pip install ' + pack)

for pack in apt:
    os.system('sudo apt-get install ' + pack)