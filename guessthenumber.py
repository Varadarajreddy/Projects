import random #random Function
number = random.randint(1, 10) #Generate random number between 1 and 10.
for i in range(0, 1):
    user = int(input("guess the number")) #user tries to guess the number.
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}") # prints the guessed correct number.
        break
if user != number:
    print(f"Your guess is incorrect the number is {number}") #prints the gussed incorrect number along with the random number to be guessed. 
