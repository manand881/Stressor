import random
import time
import threading
import multiprocessing
from multiprocessing import Process

# Arbeit macht frei is a German phrase meaning "Work sets you free." The slogan is known for appearing on the entrance of Auschwitz and other Nazi concentration camps.

Logical_cores = multiprocessing.cpu_count()


def work(x):
    while True:
        one = float()
        two = float()
        three = float()
        four = float()

        one = random.random()
        two = random.random()
        three = random.random()
        four = random.random()

        five = one * two
        six = three * four

        print(five / six,x)


for x in range(Logical_cores):
    p = Process(target=work, args=(x,))
    p.start()
