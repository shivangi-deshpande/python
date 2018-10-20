# # def findNumber():
# #     for num in range(2000,3201):
# #         if num % 7 == 0 and num % 5 != 0:
# #             print(num,end=",")
# #
# # findNumber()
#
#
# def GCD(n1, n2):
#     x, y = n1, n2
#     t = 0
#
#     while y != 0:
#         t = y
#         y = x % y
#         print(y)
#         x = t
#
#     return x
#
#
#
# def GCDR(n1, n2):
#     if n2 == 0:
#         return n1
#     return GCDR(n2, n1%n2)
#
# print(GCDR(44, 66))


def fibo(n):
    f1, f2, f3 = 0, 1, 0

    while f1 < n:
        f3 = f1
        yield f3
        f1 = f2
        f2 = f3 + f1

for i in fibo(10):
    print(i,end=" ,")
