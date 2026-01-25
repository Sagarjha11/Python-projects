def factorial(num):
    if num == 1:
        return 1
    else:
        Result = num * factorial(num - 1)
        return  Result
num = int(input("enetr number: "))
print(f"factorial is {factorial(num)}")
