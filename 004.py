#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 0 and not 6 <= n <= 20:
        print("Not Weird")
    else:
        print("Weird")
