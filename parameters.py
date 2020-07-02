# def greet(lang):
#     if lang == "es":
#         print("Hola!")
#     elif lang == "fr":
#         print("Bonjour!")
#     elif lang == "de":
#         print("Hallo!")
#     else:
#         print("Hello!")
# greet("es")
# greet("fr")
# greet("de")
# greet("en")


#try with an input?

# lang = input("What language do you speak? ")
# def greet(lang):
#     if lang == "español":
#         print("Hola!")
#     elif lang == "français":
#         print("Bonjour!")
#     elif lang == "deutsch":
#         print("Hallo!")
#     else:
#         print("Hello!")
# greet(lang)

# def greet():
#     return "Hello"
#
# print(greet(), "Joe")
# print(greet(), "CJ")


# lang = input("What language do you speak? ")
# def greet(lang):
#     if lang == "español":
#         print("Hola!")
#     elif lang == "français":
#         print("Bonjour!")
#     elif lang == "deutsch":
#         print("Hallo!")
#     else:
#         print("Hello!")
# print(greet(lang), "Joe")

# lang = input("What language do you speak? ")
# def greet(lang):
#     if lang == "español":
#         return "Hola"
#     elif lang == "français":
#         return "Bonjour"
#     elif lang == "deutsch":
#         return "Hallo"
#     else:
#         return "Hello"
# print(greet(lang), "Joe!")

# def addition(x, y):
#     sum = x + y
#     return sum
#
# a = addition(5, 8)
# print(a)

# def addition(x, y, z=9):
#     return x + y + z
#
# a = addition(3,4)
# print(a)

def addition(x, y, z=2, a=3):
    return x + y + z * a
print(addition(1, 2, a=6))
