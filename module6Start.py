# Завдання 1

# from colorama import init, Fore


# init(autoreset=True)

# def colorText(text1,text2,text3):
#     print(Fore.BLACK + text1)
#     red = Fore.RED + text2 + Fore.RESET
#     red1 = Fore.RED + text3 + Fore.RESET
#     print(f"{red} you {red1}, you are insulting yourself.")
#     print("Bill Gates")
    


# colorText("\"Don't compare yourself with anyone in this world…","if","do so")

# print(Fore.BLUE + 'some red text')
# print(Back.BLACK + 'and with a green background')

# print('back to normal now')





# ====================================================================================
# Завдання 2


# def Nums2(num1,num2):
#     for i in range(num1,num2):
#         if i % 2==0:
#             print(i)
            
# Nums2(1,19)

# =======================================================================================

# Завдання 3


# def draw(length,symbol,filled):
    
#     if filled:
#         for i in range(length):
#             print(symbol * length)
#     else:
#         print(symbol * length)
#         for i in range(length -2):
#             print(symbol + ' ' * (length - 2) + symbol)
#         print(symbol*length)

# draw(8,'*',True)
# draw(9,'@',False)

# ========================================================================

# Завдання 4


# def minimal(num1,num2,num3,num4,num5):
#     list1 = [num1,num2,num3,num4,num5]
#     print(min(list1))
    
# minimal(12,435,67,23,84)



# ===========================================================================

# Завдання 5

# def multiply(num1,num2):
    
#     if num1 > num2:
#         num1,num2 = num2,num1
#     result = 1
#     for i in range(num1,num2 +1):
        
#         result *=i
#     print(result)

# multiply(5,25)
            
            

# ====================================================================================
# Завдання 6

# def numLen(num1):
#     lenn = len(str(num1))
#     print(lenn)
# nums = int(input("enter your number :"))
# numLen(nums)

# ===========================================================================================

# Завдання 7


# def numLen(num1):
#     str1 = str(num1)
#     if str1[::1] == str1[::-1]:
#         print(True)
#     else:
#         print(False)
    
# nums = int(input("enter your number :"))
# numLen(nums)

