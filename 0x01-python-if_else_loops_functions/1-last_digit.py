#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

value = abs(number)

if number < 0:
    last_digit = -1 * (value % 10)
else:
    last_digit = value % 10

if last_digit < 6 and last_digit != 0:
    print_msg = "and is less than 6 and not 0"
elif last_digit == 0:
    print_msg = "and is 0"
elif last_digit > 5:
    print_msg = "and is greater than 5"
print(f"Last digit of {number} is {last_digit} {print_msg}")
