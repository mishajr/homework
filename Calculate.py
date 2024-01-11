


def multi(num1,num2):
    sum1 = num1 * num2
    return sum1


def division(num1,num2):
    sum1 = num1 / num2
    return sum1 


def fact(num1):
    if num1 == 1:
        return num1
    else:
        return num1* fact(num1-1)
    


def add(num1,num2):
    sum1 = num1 + num2
    return sum1



def minus(num1,num2):
    sum1 = num1 - num2
    return sum1





def rakamakafo(num):
    if num == 1 or num == 2 or num == 4 or num == 5:
        num1 = int(input("enter one number :"))
        num2 = int(input("enter two number :"))
    if num == 3:
        num1 = int(input("enter one number :"))
        
        
    
    

        



    match num:
        case 1: print(multi(num1,num2))
        case 2: print(division(num1,num2))
        case 3: print(fact(num1))
        case 4: print(add(num1,num2))
        case 5: print(minus(num1,num2))
        
        
        case _: print("Такого варіанту не існує")


while True:
    num1= int(input("Введіть число \n1->* \n2->/ \n3->! \n4->+ \n5->- \n6->Exit \n:"))
    if num1 == 6:
        print("Exit...")
        break
    rakamakafo(num1)
