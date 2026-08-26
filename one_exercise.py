#exercise 1

# INstruction :
# you are going to  write a program that calculates the sum of all the even numbers from 1 to 100
# e.g - 2+4+6+8+10+......+98+100
# IMPORTANT ,there should only be 1 print statement in your console output.it should just print the final total and not every step of calculation

# method 1
total = 0
for number in range(2,101,2):
    total += number
print(total)

# method 2

total2 = 0
for number in range(1,101):
    if number % 2 == 0:
        total2 += number

print(total2)

# -------------------------------------------------------
# exercise 2
# Fizz Buzz Problem involves that given an integer n, for every integer i <= n, the task is to write a Python program to print,
# 'FizzBuzz' if i is divisible by 3 and 5,
# 'Fizz' if i is divisible by 3,
# 'Buzz' if i is divisible by 5

for i in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizzzz")
    elif number % 5 == 0:
        print("Buzzz")
    else:
        print(number)
