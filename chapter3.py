# x = int(input("How many hours did you work?"))
# rate = 15
# pay = x * rate
# print(f"This week you made ${pay}")

# x = int(input("How many hours did you work?"))
# rate = 10
# if x <= 40:
#     pay = x * rate
# if x > 40:
#     ot = (x-40) * rate * 1.5
# totalpay = pay + ot
# print(f"This week you made ${totalpay}")

try:
    x = float(input("How many hours did you work? "))
    rate = 10.0
    if x > 40:
        pay = 40*rate + (x-40)*rate*1.5
    else:
        pay = x * rate
    print(f"This week you made ${pay}!")
except:
    print("Error: please enter numeric input")
