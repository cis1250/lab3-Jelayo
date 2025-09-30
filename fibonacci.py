fib = input("How many terms of the Fibonacci sequence would you like?")
if int(fib) <= 0:
    print("Pick a number greater than 0")
else:
    x = 0
    y = 1
    z = 0
    print("0")
    for z in range (int(fib)):
        x, y = y, x + y
        print(x)
