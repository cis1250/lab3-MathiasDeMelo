#!/usr/bin/env python3
a = 0
b = 1

def get_user_input():

  n = int(input("enter the number of terms in the fibonacci sequence"))

  if n > 0:
    return n
  else:
    print("please enter a valid interger")


num_terms = get_user_input()


for j in range(num_terms):
  print(a, end=" ")
  a = b 
  b = a + b

print()
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
