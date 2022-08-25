#!/bin/python3
from collections import OrderedDict
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    dictionary = {}
    for i in sorted(s):
        if i in dictionary:
            dictionary[i]+= 1
        else:
            dictionary[i] = 1
    # print(dictionary)
    values = sorted(dictionary.keys(), key = dictionary.get, reverse = True)
    # keys = sorted(values)
    # print(values)
    for keys in values[:3]:
        print(keys, dictionary[keys])
