# x = int(input("Choose a number greater than zero "))
# if x < 10:
#     print("That's a small number")
# elif x < 50:
#     print("That's a decent sized number")
# elif x < 100:
#     print("That's a pretty big number")
# else:
#     print("Woah! That's a very large number!")
# print("Thanks for participating!")

#what happens if the user enters something like "five"?

# try:
#     x = int(input("Choose a number greater than zero "))
#     if x < 10:
#         print("That's a small number")
#     elif x < 50:
#         print("That's a decent sized number")
#     elif x < 100:
#         print("That's a pretty big number")
#     else:
#         print("Woah! That's a very large number!")
#     print("Thanks for participating!")
# except:
#     print("That isn't a number")

try:
    x = int(input("Choose a number greater than zero "))
    if x < 10:
        print("That's a small number")
    elif x < 50:
        print("That's a decent sized number")
    elif x < 100:
        print("That's a pretty big number")
    else:
        print("Woah! That's a very large number!")
except:
    try:
        x = int(float(x))
        if x < 10:
            print("That's a small number")
        elif x < 50:
            print("That's a decent sized number")
        elif x < 100:
            print("That's a pretty big number")
        else:
            print("Woah! That's a very large number!")
    except:
        print("That isn't an integer")
print("Thanks for participating!")

#revisit later
