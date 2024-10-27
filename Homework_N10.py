# Exercise N1

# ls1 = [1, 2, 3]
# ls2 = ['a', 'b', 'c']
# ls = list(zip(ls1, ls2))
# print(ls)

# Exercise N2
#
# ls1 = [1, 2, 3, 4, 5, 6, 7]
# ls = list(filter(lambda x: x % 2 == 0, ls1))
# print(ls)

# Exercise N3

# ls1 = [-1, -2, 5, 10, -47, 1, 0]
# ls = list(filter(lambda x: x > 0, ls1))
# print(ls)

# Exercise N4

# ls1 = ['aba', 'house', 'ride', 'wide']
# ls = list(filter(lambda x: x == x[::-1], ls1))
# print(ls)

# Exercise N5

# from functools import reduce
#
# ls = [1, 2, 3, 4, 5]
# try:
#     for i in ls:
#         if not isinstance(i, int):
#             raise TypeError
#     ls1 = reduce(lambda a, b: a * b, ls)
#     print(ls1)
#
# except TypeError as e:
#     print("Type Error")

# Exercise N6

# ls = ['hello world', 'coding', 'nod']
# st = 'ing'
#
# try:
#     if not isinstance(st, str):
#         raise TypeError
#     for i in ls:
#         if not isinstance(i, str):
#             raise TypeError
#     ls_filtered = list(filter(lambda x: x[len(x)-len(st):] == st, ls))
#     print(ls_filtered)
# except TypeError as t:
#     print("Invalid")

