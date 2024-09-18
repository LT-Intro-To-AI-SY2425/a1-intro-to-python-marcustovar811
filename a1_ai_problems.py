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

## AI Problem #1, "Prime Number Finder", created by ChatGPT

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

## AI Problem #2, "Anagram Checker", created by ChatGPT
def are_anagrams(s1, s2):
    # Normalize the strings by converting to lowercase and removing spaces
    s1_normalized = s1.replace(" ", "").lower()
    s2_normalized = s2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(s1_normalized) == sorted(s2_normalized)

## AI Problem #3, "Vowel Checker", created by ChatGPT

def count_vowels(s):
    # Define the set of vowels
    vowels = "aeiouAEIOU"
    
    # Initialize a counter
    count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            count += 1  # Increment the counter
    
    return count
