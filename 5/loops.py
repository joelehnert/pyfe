#repeated steps
# Loops (repeated steps) have iteration variables that change each time through
#  loop. Often these iteration variables go through a sequence of numbers

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)



#infinite loop
# n = 5
# while n > 0:
#     print("Lather")
#     print("Rinse")
# print("Dry off!")
# we need an iteration variable to change each time through a loop!!

#there are some statements we can use to get out of a Loops
# The *break* statement ends the current loop and jumps to the statement
#  immediately following the Loops

#It is like a loop test that can happen anywhere in the body of a Loops

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print("Done!")
