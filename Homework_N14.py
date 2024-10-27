# Exercise N1
# import random
#
#
# class BankAccount:
#
#     def __init__(self, number, name, balance):
#         self.account_number = number
#         self.account_holder = name
#         self.balance = balance
#
#     def transaction(self, funds):
#         self.balance += funds
#         return f"Balance Updated: {self.balance}"
#
#     def withdraw(self, funds):
#         self.balance -= funds
#         return f"Balance Updated: {self.balance}"
#
#
# def account_number_gen():
#     num = ""
#     for i in range(10):
#         num += str(random.randint(0, 9))
#     return num
#
#
# obj1 = BankAccount(account_number_gen(), "Nika", 100)
# print(obj1.account_holder)
# print(obj1.transaction(150))
# print(obj1.withdraw(110))
#
# obj2 = BankAccount(account_number_gen(), "Noza", 200)
# print()
# print(obj2.account_holder)
# print(obj2.withdraw(50))
# print(obj2.withdraw(73))
# print(obj2.transaction(18))


# Exercise N2
#
# class Student:
#
#     def __init__(self, name, student_id, course):
#         self.name = name
#         self.student_id = student_id
#         self.course = course
#
#     def info(self):
#         return (f"""Student Id: {self.student_id}
# Student Name: {self.name}
# Courses: {self.course}""")
#
#     def courses(self):
#         for i in self.course:
#             print(i)
#
#
# stud = Student("nika", 1, ['Calculus', 'Python'])
# print(stud.info())
# stud.courses()
#
# print()
# stud1 = Student('Noza', 2, ['C++', 'Statistics'])
# print(stud1.info())
# stud1.courses()