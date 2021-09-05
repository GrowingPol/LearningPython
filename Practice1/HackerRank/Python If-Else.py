#!/bin/python

import math
import os
import random
import re
import sys

from distlib.compat import raw_input

if __name__ == '__main__':
    # Input a number between 1 and 100, If there is an invalid output. ask for a new input
    while True:
        try:
            n = int(raw_input("Input a number, please: ").strip())
            if n >= 1 and n <= 100:
                break
            else:
                print("Please, input a number within the range")
        except Exception as e:
            print("Input a valid number please, Error: ", e)

    # Clasify numbers:
    if n % 2 > 0:
        # all odd numbers are weird
        print("Weird")
    else:
        # Even numbers where 5<= n >=2 are Weird
        if n >= 6 and n <= 20:
            print("Weird")
        # All even numbers left are Not Weird
        elif (n >= 2 and n <= 5) or n > 20:
            print("Not Weird")