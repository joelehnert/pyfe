# print("This sentence comes before my loop")
# for i in [1,2,3,5,8,13,21]:
#     print(i)
# print("This sentence comes after my loop is complete")



largest_so_far = -1
print("We're starting with ", largest_so_far)
for x in [9, 41, 12, 3, 74, 15]:
    if x > largest_so_far:
        largest_so_far = x
    print(largest_so_far, x)
print("The largest number we saw was", largest_so_far)



#the -1 in the above program is a flag value, because we haven't seen any 
# numbers yet
