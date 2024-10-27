# Exercise N1

# x = int(input("Enter The Num: "))
#
# while x > 0:
#     print(x)
#     x -= 1
#

# Exercise N2

# total_sum = 0
# while True:
#     num = input("Num: ")
#     if num == 'sum':
#         print(total_sum)
#         break
#     elif int(num) > 0:
#         total_sum += int(num)


# Exercise N3

# import random
#
# num = random.randint(0, 20)
# lives = 3
#
# while lives > 0:
#     guess = int(input("Your Guess: "))
#     if guess == num:
#         print("Correct !")
#         break
#     else:
#         if lives - 1 == 0:
#             print("You Are Out Of Tries ")
#             break
#         if guess > num:
#             print("Your Guess Is Higher ")
#         else:
#             print("Your Guess Is Lower ")
#         lives -= 1
#
