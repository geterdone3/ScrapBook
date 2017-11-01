import threading
from random import randint
from os import *

def speak():
    for i in range(10):
        randInt = randint(1, 99)
        system("espeak 'rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump rump' -g 1 -p " + str(randInt) + " -s 250")
    
threads = [threading.Thread(target=speak) for i in range(250)]

for thread in threads:
    thread.start()
