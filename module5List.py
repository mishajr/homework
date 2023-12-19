# Завдання 1(перший варіант)

# arithmetic = input("Enter your arithmetic expression :").split()

# num1 = float(arithmetic[0])
# operator = arithmetic[1]
# num2 = float(arithmetic[2])

# match operator:
#     case '+': result = num1 + num2
#     case '-': result = num1 - num2
#     case '/': result = num1 / num2
#     case '*': result = num1 * num2
    
# print("Результат:", result)
#     # if operator == '+':
#     #     result = num1 + num2
#     # elif operator == '-':
#     #     result = num1 - num2
#     # elif operator == '*':
#     #     result = num1 * num2
#     # elif operator == '/':
#     #     if num2 != 0:
#     #         result = num1 / num2
#     #     else:
#     #         print("Ділення на нуль неможливе.")
#     #         result = None




# Завдання 1 (2 варіант)

# arithmetic = input("Enter your arithmetic expression :")

# print(eval(arithmetic))


# ====================================================================================================

# Завдання 2

# import random



# list1 = [i + random.randint(-50,50) for i in range(20)]


# print(f"Мінімальне значення :{min(list1)}")
# print(f"Максимальне значення :{max(list1)}")

# sumPlus = 0
# sumMinus = 0
# sumNull = 0
# list2 = []
# for i in list1:
#     if i > 0:
#         sumPlus+=1
        
#     if i < 0:
#         sumMinus+=1
#     if i == 0:
#         sumNull+= 1
# print(f"Сума мінусових чисел :{sumMinus}")
# print(f"Сума плюсових чисел :{sumPlus}")
# print(f"Сума нулів :{sumNull}")
     

# ====================================================================================================

# Завдання 3



# import random

# list1 = [i + random.randint(0,50) for i in range(10)]
# list2 = [i + random.randint(0,50) for i in range(10)]
    
    
# list3 = list1 + list2
# print(list3)

# list45 = list1 + list2
# print(list(set(list45)))

# setList1 = list(set(list1))
# setList2 = list(set(list2))
# listSum = setList1 + setList2
# print(listSum)


# list5 =[i for i in list1 if i in list2]
# print(list5)


# list1MaxMin = [max(list1),min(list1)]
# list2MaxMin = [max(list2),min(list2)]
# list10 = list1MaxMin + list2MaxMin
# print(list10)
















    
    
