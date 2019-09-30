# Guessing a random number

# Testing a few strategies to guess a randomly generated number

Three strategies are compared to each other. The strategies are:
* Incremental guessing
* Randomly guessing
* Guessing assuming the randomly generated number have approximately the same number of bits set to 1 and set to 0

The result of the methods are plotted in the attached graph for guessing a number consisting of 16 bits. Each method is tested 500 times. The random guessing is by far a much worse strategy than iterating from zero up to the secret number. The attempt to create smarter guesses by assuming a random number would approximate have the same number of 1 and 0 bits set did not yield a better guessing strategy than just straight forward increment your guess starting from the number 0.

Run the experiment by executing main in python 2.x and in the input argument, specify the number of bits in the number you want to guess should consist of.

```
>>> python main.py 16
```

*Requirements: Matplotlib and Numpy *
