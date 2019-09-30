#!/usr/bin/python

import sys

bits = sys.argv[1]
max_val = 2**int(bits)

x = []
y = []
print_format = '0'+ bits +'b'
i = 0
fd = open("points.log", "w")
while i < max_val:
    # if i%1000000 == 1:
    #     print(str(i) + " / " + str(max_val))
    b = format(i, print_format)
    ones = b.count("1")
    fd.write(str(i) + " " + str(ones) + "\n")

    i+=1

fd.close()
