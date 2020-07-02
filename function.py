# def thing():
#     print("Joe")
#     print("LOL")
#
# thing()
# print("OKAY!?")
# thing()

#a function is a bit of reusable code -  def keyword(parameters):,
#then we call or invoke to tell when to use the function
#functions take some input and then produce an output

# big = max(1,4,5,37)
# print(big)
# small = min(1,4,5,37)
# print(small)

# x = 5
# print('Hello')
#
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day")
#
# print("Yo")
# x = x + 2
# print(x)

#the problem with the above code is that you never invoked the function. You
# defined it, but nowhere did you call for it to run
# you've got the define part, but not the reuse part!!

x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day")

print("Yo")
print_lyrics()
x = x + 2
print(x)

#you can define arguments using the parentheses
