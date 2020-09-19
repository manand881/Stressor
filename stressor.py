import random
import time
import multiprocessing
from multiprocessing import Process

# Arbeit macht frei is a German phrase meaning "Work sets you free." The slogan is known for appearing on the entrance of Auschwitz and other Nazi concentration camps.

Logical_cores = multiprocessing.cpu_count()         # counting the number of logical cores in the system
Pros = []                                           # declaring a variable which acts as a list of processes


def work():
    zero = list()                                   # creating a list to hold floating point operation results to stress memory
    while True:
        one = float()                               # creating empty variables later to be used as an extra step before it is reassigned in the random function
        two = float()
        three = float()
        four = float()

        one = random.random()                       # storing random floating point values
        two = random.random()
        three = random.random()
        four = random.random()

        five = one * two                            # distilling it down to two values and adding an extra step in the between
        six = three * four

        zero.append(five + six)                     # performing floating point operations to stress CPu
        zero.append(five - six)
        zero.append(five * six)
        zero.append(five / six)


if __name__ == '__main__':
    for x in range(Logical_cores):                  # creating processes to match the number of logical cores of the system
        p = Process(target=work)
        time.sleep(3)                               # giving the system enough time to reorganise itself and create page files for other programs.
        Pros.append(p)                              # appending list of processes to the before mentioned variable
        p.start()                                   # staring the processes

for t in Pros:                                      #   The liberation that shall never come
    t.join()
