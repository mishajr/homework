# Завдання 1

# try:
#     name = input("enter your name :")
#     age = int(input("Enter your age :"))
#     if age < 0 or age > 130:
#         raise ValueError()
    
# except ValueError as e:
#     print("Error")
# else:
#     print(f"Hi {name}\nYour age {age}")
    
    
    
# ===============================================================================
    
# Завдання 2,1

   

# def format_greeting(name, age):
#     if age < 0 or age > 130:
#         raise ValueError()
    
#     return f"Привіт, {name}! Твій вік — {age}"


# try:
#     name = input("Введіть ім'я: ")
#     age = int(input("Введіть вік: "))
#     greeting = format_greeting(name, age)
#     print(greeting)

# except ValueError as e:
#     print(f"Помилка")

# Завдання 2,2



# def format_greeting(name, age):
    
#     try:
#         if age < 0 or age > 130:
#             raise ValueError('Value Error')
#         return f"Привіт, {name}! Твій вік — {age}"
        
#     except ValueError as e:
#         return f"Помилка {e}"

# name = input("Введіть ім'я: ")
# age = int(input("Введіть вік: "))

# greeting = format_greeting(name, age)
# print(greeting)


# ===============================================================================



# завдання 3

# try:
#     input_numbers = input("Введіть числа через пробіл: ")
#     numbers = [int(i) for i in input_numbers.split()]
#     for i in numbers:
#         if i < 0:
#             raise ValueError("число меньше нуля")
        
#     print(f"Сума всіх названих вами чисел = {sum(numbers)}")
            
   
    
# except ValueError as e:
#     print(f"Помилка! - {e}") 

 
# ===============================================================================

# Завдання 4.1


# def format_greeting(numbers):
#     for i in numbers:
#         if i < 0:
#             raise ValueError("число меньше нуля")
        
#     return f"Сума всіх названих вами чисел = {sum(numbers)}"

# try:
#     input_numbers = input("Введіть числа через пробіл: ")
#     numbers = [int(i) for i in input_numbers.split()]

#     greeting = format_greeting(numbers)
#     print(greeting)

            
   
    
# except ValueError as e:
#     print(f"Помилка! - {e}") 



# Завдання 4.2



# def format_greeting(numbers):
    
#     try:
#         for i in numbers:
#             if i < 0:
#                 raise ValueError("число меньше нуля")

#         for i in numbers:
#             if i < 0:
#                 raise ValueError("число меньше нуля")            
#         return f"Сума всіх названих вами чисел = {sum(numbers)}"
    
#     except ValueError as e:
#         return f"Помилка! - {e}" 

# input_numbers = input("Введіть числа через пробіл: ")
# numbers = [int(i) for i in input_numbers.split()]
    
# greeting = format_greeting(numbers)
# print(greeting)   
 
    








