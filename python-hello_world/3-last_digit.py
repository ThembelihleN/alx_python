#python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
else:
    ("Last digit of {} is {} and is less than 6 and not zero".format(number, last_digit))
