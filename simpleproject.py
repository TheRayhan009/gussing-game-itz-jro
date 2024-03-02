print("_____________________________________________________")
print("|                 ASSALAMUALAIKUM                   |")
print("|        Welcome to a number gussing game !         |")
print("|           [][]   ABOUT CREATOR [][]               |")
print("|             #    FB : Itz Jro                     |")
print("|             #   Noob in Python                    |")
print("|             #     A Hablu :)                      |")
print("|                                                   |")
print("| *?* How to play : Guess any number. Follow the    |")
print("|     commands of the programme. Say the programme  |")
print("|     that you have followed the instruction using  |")
print("|     y/n. Here y is for Yes and n is for No. ENJOY!|")
print("|                                                   |")
print("| %Note: Vul truti hole khomar chokhe dekhben :)    |")
print("_____________________________________________________")
print()
print()

# Heading

v = str(input(" [<][>] Do you want to continue ? ( y/n ) :"))

if v == 'y':
    print("Let's Start the game")
    print()
    print("___Think a number between 1 - 100")
    print()
elif v == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Starting the game by subtracting 1

v1 = str(input("___Do you thought a number between 1 to 100 ? ( y/n ) :"))

if v1 == 'y':
    print("___Now subtract 1 from the number")
    print()
elif v1 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Multiplication

v2 = str(input("___Do you subtracted 1 from the number? ( y/n ) :"))

if v2 == 'y':
    print("___Now Multiply the number with 3")
    print()
elif v2 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Adding 12

v3 = str(input("___Do you multiplied 3 with the number? ( y/n ) :"))

if v3 == 'y':
    print("___Now add 12 with the number")
    print()
elif v3 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Divideing 3

v4 = str(input("___Do you added 12 with the number? ( y/n ) :"))

if v4 == 'y':
    print("___Now divide the number by 3")
    print()
elif v4 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Add 5

v5 = str(input("___Do you divided the number by 3? ( y/n ) :"))

if v5 == 'y':
    print("___Now add 5 with the number")
    print()
elif v5 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# subtract the number from original number

v6 = str(input("___Do you added 5 with the number? ( y/n ) :"))

if v6 == 'y':
    print("___Now subtract the number from the original number that you thought at first")
    print()
elif v6 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

# Showing result

v7 = str(input("___Do you subtracted the number from original number? ( y/n ) :"))

if v7 == 'y':
    print()
    print()
    print("____________________")
    print("|__THE RESULT IS 8__|")
    print("____________________")
    print()
    print()
elif v7 == 'n':
    print("Its look like you dont want to continue, Bye")
    exit()
else:
    print("Wrong Input")
    exit()

#asking about it

m = str(input("__Can you give me the number that you thought at first so that I can explain the whole matter ?[] OPTIONAL [] ( y/n ) :"))
if m == 'y':
    print("Let's Give you full summary")
    print()
elif m == 'n':
    print("It's ok! Thanks for playing this simple game. Have a great day!")
    exit()
else:
    print("Wrong Input")
    exit()
# Find full history

a = int(input("Give me the number that you thought at first (Optional) :"))
print()
# Some maths :)

b = a - 1
c = b * 3
d = c + 12
e = d / 3
f = e + 5
g = f - a

# Giving Full summary
print("___THIS IS THE FULL SUM WITH EXPLANATION___")
print()
print(f"Your guessed number was {a}. After subtract 1 from the number the number is {b}.")
print(f"Then after multiplying the number with 3 the number became {c}.")
print(f"Adding 12 the number became {d}")
print(f"Dividing the number by 3 the number become {int(e)}")
print(f"After adding 5 with your guessed number the number is {int(f)}")
print(f"At last subtracting this number from the guessed number you guess at first, The result is {int(g)}")
print()
print()
print("SOME WORDS OF CREATOR")
print()
print("This whole game is created by a noob programmer name Jubair Rahman.Facebook : Itz Jro and ")
print("Telegram : @master_trader44. If you feel happy to play this simple game than give it a ")
print("rateing :) . If you feel bad then please forgive me because I am totally noob i python. ")
print("At last thank you again for playing this simple game. Have a great day! Assalamualaikum. ")











