
num = int(input("Enter the max range:")) #Request for the user input.
for i in range(num):
    if i % 5 == 0 and i % 3 == 0: # prints FizzBuzz if the number is divisble by 5 and 3.
        print("FizzBuzz")
    elif i % 3 == 0: #prints Fizz if the number is divisible by only 3.
        print("Fizz")
    elif i % 5 == 0: # prints if the number is divisible by only 5.
        print("Buzz")
    else: #prints the only given number.
        print(i)
