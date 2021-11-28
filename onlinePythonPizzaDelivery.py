print("Welcome to online python pizza deliveries!")
size=input("Please enter your choice of pizza size S, M, L \n ")
pepproni=input("Do you want to add Pepproni to your pizza? Y or N\n")
extra_cheese=input("Do you want to add extra cheese to your pizza? Y or N\n")
bill=0
if size=="S":
    bill=15
    if pepproni == "Y" and extra_cheese== "N":
        bill=bill+2
        print(f"Your total bill is {bill}")
    elif pepproni=="N" and extra_cheese=="Y":
        bill=bill+1
        print(f"Your total bill is {bill}")
    elif pepproni=="Y" and extra_cheese=="Y":
        bill=bill+1+2
        print(f"Your Total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")

elif size=="M":
    bill=20
    if pepproni == "Y" and extra_cheese== "N":
        bill=bill+3
        print(f"Your total bill is {bill}")
    elif pepproni=="N" and extra_cheese=="Y":
        bill=bill+1
        print(f"Your total bill is {bill}")
    elif pepproni=="Y" and extra_cheese=="Y":
        bill=bill+3+1
        print(f"Your Total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")

elif size=="L":
    bill=25
    if pepproni == "Y" and extra_cheese== "N":
        bill=bill+3
        print(f"Your total bill is {bill}")
    elif pepproni=="N" and extra_cheese=="Y":
        bill=bill+1
        print(f"Your total bill is {bill}")
    elif pepproni=="Y" and extra_cheese=="Y":
        bill=bill+3+1
        print(f"Your Total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")

else:
    print("Please select the size of your pizza and try again!")