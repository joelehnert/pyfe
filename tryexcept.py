#a way to eliminate or catch a traceback

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)

#error handling/handling exceptions
