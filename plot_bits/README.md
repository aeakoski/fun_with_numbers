# Plot the number of bits set to 1 for all the numbers

To generate a plot run main.py which yields a points.log file. This file contains the datapoints that can be ploted by gnuplot. Matplotlib is too slow and cant plot these large datafiles.


main.py takes an argument consisting of the number of bits in the max value to plot the bits for.


The bit representation of the numbers generated inside the program will be padded with zeros until the bit size is the same as specified in the initial argument.

```
>>> python main.py 16
>>> gnuplot
>>> >>> plot 'points.log'
```
