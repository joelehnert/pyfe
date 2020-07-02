#counting number of items in a set
# count = 0
# print("Starting:", count)
# for i in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     print(count, i)
# print("Our total count is", count)

#summing in a loop
# # to add up a value we encounter in a loop, we introduce a sum variable that
# #  starts at 0 and we add the value to the sum each time through the loop
#
# total = 0
# print ("What do all these numbers add up to?")
# for j in [9, 41, 12, 3, 74, 15]:
#     total = total + j
#     print(total, j)
# print("The sum is", total)
#
# # finding the average in a loop
# count = 0
# total = 0
# for k in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     total = total + k
#     average = total / count
# print("The average is", average)
#
# # filtering in a loop
# for l in [9, 41, 12, 3, 74, 15]:
#     if l > 20:
#         print("Large number detected!", l)

#search using a boolean variable
# found = False
# for m in [9, 41, 12, 3, 74, 15]:
#     if m == 3:
#         found = True
# if found == True:
#     print("We found a 3!")
# else:
#     print("There were no 3's found")

#you can also change the above by putting a break after you find a 3 so that
#the program doesn't continue to run!

#how do we find the smallest number in a set?
# use the None variable, which only has one constant in it
# booleans have true or false, integers have a whole bunch, floats have
#  a whole bunch, None we think of as the lack of a value

smallest = None
for n in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
print("The smallest number in the list is", smallest)
