def factorial(num):
    fac = 1
    for i in range(1, num+1):
        fac *= i

    return fac

x = int(input("Enter the Number"))

print(factorial(x))


