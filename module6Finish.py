# Завдання 1

# def multiply(list1):
    
#     result = 1
#     for i in list1:
#         result *= i
#     return result
        
        
# list1=[2,3,4,5]
# result = multiply(list1)


# ===============================================================

# Завдання 2 

# def minimal(list1):
    
#     return min(list1)
    
# list1 = [32,67,13,56]
# result = minimal(list1)
# print(result)


# ====================================================================

# Завдання 3


# def nums(num):
    
#     if num < 2:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
        
# def lists(list1):
#     count = 0
#     for i in list1:
#         if nums(i):
#             count +=1
#     return count

# list2 = [2,3,4,5,6,7,11,13]
# result = lists(list2)
# print(f"Кількість простих чисел у списку : {result}")


# =======================================================================

# Завдання 4

# def deL(num):
#     list1 = [3,5,7,5,65,5,546,5,56,13]
#     ref = list1.count(num)
    
#     for i in list1:
#         if i == num:
#             list1.remove(num)
#     print(f"Видалених елементів :{ref} \nВидалени елемент :{num} \n {list1}")
    
# deL(3)
   
# ==============================================================================
# Завдання 5

# def lists(list1,list2):
#         marge = list1 + list2
#         return marge


# list1 = ["dfsdfsdf",345,123]
# list2 = ["sdf",3412,13]
# fullist = lists(list1,list2)
# print(fullist)


# ======================================================================================
# Завдання 6
# def stupin(list1,num):
    
#     degree = [i ** num for i in list1]
#     return degree

# listDegree = [4,3,6,2,5]
# result = stupin(listDegree,6)
# print(result)











