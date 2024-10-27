# Exercise N1

# squared_numbers = set()
# for i in range(1,11):
#     squared_numbers.add(i ** 2)
# print(squared_numbers)

# Exercise N2

# st = set()
# word = input("Enter the Word: ")
# for i in word:
#     st.add(i)
# print(st)

# Exercise N3

# tuple1 = (1, 2, 3, 4, 5, 6)
# tuple2 = (4, 5, 5, 6, 6, 7)
# combined = tuple1 + tuple2
# ls = list(set(tuple1) & set(tuple2))
# print(tuple(set(combined)))
# print(ls)

# Exercise N4

# tpl = (1, 2, 3, 4)
# ls = list(tpl)
# ls1 = ls.copy()
# ls[0] = ls1[-1]
# ls[-1] = ls1[0]
# tpl = tuple(ls)
# print(tpl)

# Exercise N5

# tp = (1, (2, 3), (4, (5, 6)))
# output = []
# for element in tp:
#     if isinstance(element, tuple):  # If the element is a tuple
#         for subelement in element:
#             if isinstance(subelement, tuple):  # Check if it has a deeper level of nesting
#                 for subsubelement in subelement:
#                     output.append(subsubelement)
#             else:
#                 output.append(subelement)
#     else:
#         output.append(element)
# output = tuple(output)
# print(output)

# Exercise N6
#
# set1 = {1, 2}
# set2 = {'a', 'b'}
# output_set = set()
# for x in set1:
#     for y in set2:
#         output_set.add((x, y))
# print(output_set)
