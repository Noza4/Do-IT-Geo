# Exercise N1

# file = open('test.txt', 'w')
# for i in range(1, 1001):
#     file.write(f'Line {i}\n')
# file.close()
# file = open('test.txt', 'r')
# print(len(file.readlines()))

# Exercise N2

# file = open('test1.txt', 'w+')
# for i in range(1, 20):
#     if i == 2:
#         file.write('ori\n')
#     elif i == 8:
#         file.write('rva\n')
#     elif i == 10:
#         file.write('ati\n')
#     elif i == 13:
#         file.write('cameti\n')
#     elif i == 17:
#         file.write('chvidmeti\n')
#     else:
#         file.write('\n')
# file.close()
# file = open('test1.txt', 'r')
# for _ in range(20):
#     print(file.readline())
# file.close()

# Exercise N3

# file1 = open('file1.txt', 'w')
# file1.write('pirveli faili')
# file1.close()
# file2 = open('file2.txt', 'w')
# file2.write('meore faili')
# file2.close()
#
# with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('combine.txt', 'w+') as combine:
#     combine.writelines(file1.readline())
#     combine.write('\n')
#     combine.writelines(file2.readlines())
#
# file = open('combine.txt', 'r')
# print(file.read())

# Exercise N4

# with open('palindrome.txt', 'w+') as file:
#     file.write('ana\n')
#     file.write('car\n')
#     file.write('level\n')
#     file.write('mister\n')
#
# with open('palindrome.txt', 'r') as file:
#     for _ in range(1, 5):
#         word = file.readline().strip()
#         if word == word[::-1]:
#             print(word)

# Exercise N5

# def manager(name):
#     with open(name, 'r') as file:
#         quantity = len(file.readlines())
#     with open(name, 'r') as file:
#         for i in range(quantity // 10):
#             filename = f'f{i}'
#             with open(filename, 'w') as f:
#                 for _ in range(10):
#                     f.write(file.readline())
#                     f.write('\n')
#
#
# with open('testing.txt', 'w') as file:
#     for i in range(33):
#         file.write(f'{i}\n')
# with open('testing.txt', 'r') as file:
#     for i in range(33):
#         print(file.readline())
# manager('testing.txt')

# Exercise N6

# def func(f1, f2):
#     with open(f1, 'r') as file:
#         quantity = len(file.readlines())
#     with open(f1, 'r') as file, open(f2, 'w+') as f:
#         for i in range(quantity):
#             f.write(file.readline().strip())
#
#
# with open('text.txt', 'w') as file:
#     file.write('erti\n')
#     file.write('meore\n')
#     file.write('mesame\n')
#
# func('text.txt', 'text1.txt')
