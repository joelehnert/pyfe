#Python has a number of string functions which are in the string library
#These functions are already built into every string - we ivoke them by
#  appending the function to the string variables
#These functions do not modify the original string, instead they return a new
#  string that has been altered

# greeting = "Hello, Joe"
# mod = greeting.lower()
# print(mod)
#
# print(greeting)
#
# print("Hi CJ!".lower())

# thing = "Hello, Joe"
# x = type(thing)


# https://docs.python.org/3/library/stdtypes/html#string-methods
# tells what parameters are

# print(thing.upper())

#Searching a string
#We use the find() function to search for a substring within another string
#find() finds the first occurrence of the substring
#If the substring is not found, find() returns -1
#Remember that string position starts at 0

# fruit = "papaya"
# pos = fruit.find("pa")
# print(pos)
#
# lie = fruit.find("pai")
# print(lie)

#Search and replace
#The replace() function is like a "search and replace" operation in a word processor
#It replaces all occurences of the search string with the replacement strings

# greeting = "Hello, Joe"
# newgreet = greeting.replace("Joe","CJ")
# print(newgreet)
#
# newgreety = greeting.replace("o", "u")
# print(newgreety)

haystack = "papaya"
needle = "ya"
def find(needle, haystack):
    x = 0
    y = len(needle)
    while y < len(haystack)+1:
        if needle == haystack[x:y]:
            return x
        x = x+1
        y = y+1
    return -1
a = find(needle, haystack)
print(a)



needle = "aaab"
haystack = "aaaaaaaaaaaaaaaaaaaaaab"
