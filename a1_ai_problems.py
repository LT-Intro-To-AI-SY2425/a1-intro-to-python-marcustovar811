# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

## AI Problem #1, "Prime Number Finder"

import math
10
print("Input your number")
num = int(input())
if(num <= 1):
    print ("False")
elif(num == 2):
    print ("True")
elif(num % 2 == 0):
    print ("False")
elif():
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            print ("False") 
    print ("True")