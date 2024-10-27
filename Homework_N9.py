# Exercise N1

# def func(n):
#     global int_list
#     int_list.append(n)
#
#
# int_list = [10, 20, 30, 40]
# func(int(input("Enter the number: ")))
# print(int_list)

# Exercise N2

# def sm(number):
#     if number == 0:
#         return 0
#     else:
#         return number % 10 + sm(number // 10)
#
#
# print(sm(12345))

# Exercise N3

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
#
#
# print(reverse_string("Hello"))

# Exercise N4

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# for i in range(10):
#     print(fibonacci(i), end=" ")
