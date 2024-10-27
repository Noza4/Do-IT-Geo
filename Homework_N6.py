# Exercise N1

# word = input("Enter The Sentence: ")
# words = word.split()
# counter = {}
# for each in words:
#     counter[each] = 0
# for each in words:
#     if each in counter.keys():
#         counter[each] += 1
# print(counter)

# Exercise N2

# info = {}
# operation = input('Enter The Operation: ')
# num1 = float(input("Enter The First Number: "))
# num2 = float(input("Enter The Second Number: "))
# info[operation] = [num1, num2]
# if operation == '+':
#     answer = info[operation][0] + info[operation][1]
# elif operation == '-':
#     answer = info[operation][0] - info[operation][1]
# elif operation == '*':
#     answer = info[operation][0] * info[operation][1]
# elif operation == '/':
#     answer = info[operation][0] / info[operation][1]
# elif operation == '%':
#     answer = info[operation][0] % info[operation][1]
# else:
#     answer = "The Operation You Entered Is Not Defined"
#
# print(answer)

# Exercise N3

# dc = {key: key * key for key in range(1, 11)}
# print(dc)

# Exercise N4

workplace = {

    'Workers': {
        'Name': ['Nika', 'Dimitri'],
        'LastName': ['Nozadze', 'Beridze'],
        'Age': [20, 50],
        'Departments': ['IT', 'IT'],
        'Salary': [2000, 1000]
    }
}

total = 0
for i in workplace['Workers']['Salary']:
    total += i

print(total / 2)