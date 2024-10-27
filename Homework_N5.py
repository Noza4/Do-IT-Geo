# Exercise N1
#
# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
# sm = mylist[2] + mylist[8] + mylist[13]
# print(sm)

# Exercise N2
#
# import random
# ls = []
# ls1 = []
# mn = 101
# mx = 0
# for _ in range(20):
#     i = random.randint(0, 100)
#     ls.append(i)
#     if i % 2 == 1:
#         ls1.append(i)
#     if i < mn:
#         mn = i
#     elif i > mx:
#         mx = i
# print(mn, mx)

# Exercise N3

# ls = [43, '22', 12, 66, 210, ['hi']]
# print(ls.index(210))
# ls[len(ls)-1].append('hello')
# print(ls.pop(1))
# ls2 = ls.copy()
# ls2.clear()
# print(ls, ls2)

# Exercise N4

# ls = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
# ls1 = ls.copy()
# ls_sum = []
# if len(ls) == len(ls1):
#     for i in range(len(ls)):
#         if len(ls[i]) != len(ls1[0]):
#             print("Dimensions Aren't Same")
#             break
#         else:
#             ls_sum.append([])
#     for i in range(len(ls)):
#         for j in range(len(ls[i])):
#             ls_sum[i].append(ls[i][j] + ls1[i][j])
# print(ls_sum)

# Exercise N5

# ls = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]
#       ]
# ls1 = [[0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0]
#        ]
#
# for i in range(len(ls)):
#     for j in range(len(ls[i])):
#         ls1[j][i] = ls[i][j]
# print(ls, ls1)

# Exercise N6

# import random
# ls = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
# print(ls)