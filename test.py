import time

def rec(x):
    print ("Hello World")
    time.sleep(1)
    while x < 5:
        print (x)
        x += 1
        rec(x)

x = 0

rec(0)

print ("end")