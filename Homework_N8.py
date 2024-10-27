# Exercise N1

# def anagram(x, y):
#     if len(x) == len(y):
#         val = dict()
#         val1 = dict()
#         for i in x:
#             val.update({i: 0})
#         for i in y:
#             val1.update({i: 0})
#         for i in x:
#             val[i] += 1
#         for i in y:
#             val1[i] += 1
#         if val.keys() == val1.keys():
#             for i in val:
#                 for j in val1:
#                     if i == j:
#                         if val[i] != val1[j]:
#                             break
#                     else:
#                         continue
#         else:
#             return False
#     else:
#         return False
#     return True
#
#
# st = input("Enter the Word: ")
# st1 = input("Enter the Second Word: ")
# print(anagram(st, st1))

# Exercise N2

# def counter(x: str, y: str):
#     return x.count(y)
#
#
# word = input("Enter The Word: ")
# char = input("Enter The Symbol: ")
# print(counter(word, char))

# Exercise N3

# def fib(n):
#     ls = [0, 1]
#     for _ in range(2, n):
#         ls.append(ls[-1] + ls[-2])
#     return ls
#
#
# x = int(input("Enter the num: "))
# print(fib(x))
