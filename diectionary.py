def fun(num):
    d = dict()
    for i in range(1, num+1):
        d[i] = i**2

    return d

x = int(input("Enter the Limit = "))
print(fun(x))