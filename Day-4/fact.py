fact = int(input("enter any number:"))
factorial = 1

if fact == 0:
    print(f"the factorial of zero will be 1")
else:
    for i in range(1,fact+1):
         factorial = factorial * i
    print(f"factorial of a num is {factorial}")
