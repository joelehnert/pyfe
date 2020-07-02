# max() is a function that finds the max of something

# big = max("Hello, world!")
# print(big)
#
# small = min("Hello, world!")
# print(small)


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

greet("en")
greet("fr")
greet("es")

# Return value
# A "Fruitful" function is one that produces a result (or return value)
# The return statement ends the function execution and "sends back" the result of
#  the function

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("es"), "Joe")
print(greet("fr"), "Joe")
print(greet("en"), "Joe")


# Multiple Parameters/arguments
# *We can define more than one parameter in the function definition
# * we simply add more arguments when we call the function
# * We match the number and order of arguments and Parameters

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
