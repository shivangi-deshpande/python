
# ip = input("Enter the number = ")

l = [x for x in input("Enter the number = ").split(",")]

t = tuple(l)

print("List",l[5])
print("Tuple",t[0])

l[2] = 3
print("List",l[5])

