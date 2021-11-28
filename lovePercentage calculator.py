print("welcome to the love calculator!")
name1=input("What is your name?\n")
name2=input("What is ypur partner's name\n")
combined_string=name1+name2
lower_string=combined_string.lower()

t=lower_string.count("t")
r=lower_string.count("r")
u=lower_string.count("u")
e=lower_string.count("e")

true=t+r+u+e

l=lower_string.count("l")
o=lower_string.count("o")
v=lower_string.count("v")
e=lower_string.count("e")

love=l+o+v+e

love_score=str(true)+str(love)
new_love_score=int(love_score)

if (new_love_score<=10) or (new_love_score>=80):
    print(f"your love score is {new_love_score}% you go together like coke and mintos.")
elif (new_love_score>=40) and (new_love_score<=50):
    print(f"your love score is {new_love_score}%, you are alright together.")
else:
    print(f"Your love score is {new_love_score}%")