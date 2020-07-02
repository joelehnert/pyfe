x = 1 + 2 * 3 - 4 / 5 ** 6
print(x)

x = 1 + (2 * 3) - (4 / (5 ** 6))
print(x)

##input!!!!!!!
name = input('What is your name?')
print('Welcome,',name,'!')
#hmm, why does this print a space between my name and the exclamation point
#oh, you need to concatanate to eliminate the comma. Let's try below

nam = input('Hello! What is your name?')
print('Welcome ' + name + '!')
