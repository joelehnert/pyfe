# b a n a n a
# 0 1 2 3 4 5
# we can get at any single character in a string using an index specified
# in square brackets

# the index value must be an integer and starts at 0

# the index value can be an expression that is computed

#you will get a python error if you attempt to index past the string
# (i.e., fruit[9] as seen below, because banana doesn't have 10 characters)

# fruit = "banana"
# letter = fruit[1]
# print(letter)
#
# x = 3
# w = fruit[x-1]
# print(w)
#
# #len function - take input some parameter and produces output
#
# y = len(fruit)
# print(y)

#Looping through strings
#Using a while statement and an iteration variable and the len function, we
#can construct a loop to look at each of the letters in a string individually
#indeterminate loop

# fruit = "banana"
# index = 0
# while index < len(fruit):
#     x = fruit[index]
#     print(index, x)
#     index = index + 1

#determinate loop

# fruit = "banana"
# for letter in fruit:
#     print(letter)
#
# word = "banana"
# count = 0
# for letter in word:
#     if letter == "a":
#         count = count + 1
# print(count)
#
# for letter in "banana":
#     print(letter) #body
#letter is iteration variable, which "iterates" through the sequence (ordered set)
# -the block (body) of code is executed once for each value in the sequence

# the iteration variable moves through all of the values in the sequence ("banana")

#Slicing
#allows you to look at any continuous sectyion of a string using a colon operator
#the second number is one beyond the end of the "slice" - up to but not including
#if the second number is beyond the end of the string, you stop at the end of the strings

name = "Joe Lehnert"
print(name[0:3])
print(name[4:7])
print(name[7:50])
print(name[:])
