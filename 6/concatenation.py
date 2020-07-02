# a = "Hello,"
# b = a + "Joe"
# print(b)
#
# # the above statement won't have a space
#
# c = a + " " + "Joe"
# print(c)

#Using *in* as a logical operator
#The in keyword can also be used to check to see if one string is "in"
# another strings

#the "in" expression is a logical expression that returns True or false
# and can be used in an if statements

# fruit = "papaya"
# "p" in fruit
#
# "j" in fruit
#
# "pay" in fruit
#
# if "a" in fruit:
#     print("Yes, we found it")

#STRING COMPARISON

word = input("Name a fruit ")
if word == "papaya":
    print("All right, papaya!")
elif word < "papaya":
    print("Your fruit comes before papaya alphabetically")
else:
    print("Your fruit comes after papaya alphabetically")
