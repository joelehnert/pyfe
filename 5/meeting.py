# for i in range(1, 101):
#     if i%15 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# total = 0
# count = 0
# while True:
#     number = input("Enter a number, or type done")
#     try:
#         digit = int(number)
#         count = count + 1
#         total = total + digit
#     except:
#         if number == "done":
#             break
#         else:
#             print("Invalid input")
# print(total)
# print(count)
# average = total/count
# print(average)

total = 0
count = 0
while True:
    number = input("Enter a number, or type done ")
    try:
        digit = int(number)
        count = count + 1
        total = total + digit
    except:
        if number == "done":
            break
        else:
            print("Invalid input")
average = total/count
print(total, count, average)
