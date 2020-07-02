#x = 5
# while(x>=0):
#     print("I just ate a cookie. \nNow how many cookies are left?")
#     x = str(x)
#     print("There are " + x + " cookies left.\n")
#     x = int(x)
#     x = x - 1
# print("Now there are no more cookies :(")


#***some notes***
#the \n creates a new line in the output

#since I want to write a line that combines strings and integers, I have to
##convert the integers to strings. I tried the above method to conver them.

#what if I were just to use a separate variable as the integer form of x?
## or do I absolutely have to convert it? Let's try and find out


# x = 5
# while(x>=0):
#     print("I just ate a cookie. Now how many cookies are left?")
#     y = str(x)
#     print("There are " + y + " cookies left.\n")
#     x = x - 1
# print("Now there are no more cookies :(")

#it worked! I was able to use y to definte x as a string, and then didn't have
# to reset x as an integer after using it in the string, such as in line 7

# x = 5
# while(x>=0):
#     print("I just ate a cookie. Now how many cookies are left?")
#     print("There are " + str(x) + " cookies left.\n")
#     x = x - 1
# print("Now there are no more cookies :(")

x = 5
y = 1.5
while(x>=0):
    print("\"I just ate a cookie. Now how many cookies are left?\"")
    print(f"There are {x} cookies left, but I am going to eat {y} of them.\n")
    x = x - 1
print("Now there are no more cookies :(")
#https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
