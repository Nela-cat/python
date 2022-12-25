#Практична робота 3

#1##
# a=3
# lista=[]
# i=0
# while i<a:
#     m=int(input("a,b,c"))
#     lista.append(m)
#     i+=1
# print(lista)

# b=list(filter(lambda x:x>=1 and x<=3, lista))
# print(f"mas >=1 and <=3 {b}")

#####################################################################################

#2##
# r = int(input())
# if r % 4 != 0:
#     print('365')
# elif r % 100 != 0:
#     print('366')
# elif r % 400 != 0:
#     print('365')
# else:
#     print('366')

#####################################################################################


#3##
# a =int(input("a="))
# if a >500:
#     b=a-(a*3)/100
#     print("b=",b)
# elif a >1000:
#     b=a-(a*5)/100
#     print("b=",b)    


#####################################################################################

#4##
# a=int(input("1 - кілограм, 2 - міліграм, 3 - грам, 4 - тонна, 5 - центнер "))
# b=int(input("масa М "))

# if a==1:
#     print(f"масa:  {b} kg")

# elif a==2:
#     b=b*10**(-6)
#     print(f"масa: {b} kg")
# elif a==3:
#     b=b*10**(-3)
#     print(f"масa: {b} kg")
# elif a==4:
#     b=b*10**3
#     print(f"масa: {b} kg")        
# elif a==5:
#     b=b*10**2
#     print(f"масa: {b} kg")

#####################################################################################

#5##
# import math
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))
# d = float(input('d: '))
# if a < b and a < c and a < d :
#     print (math.cos(a))
# elif b < a and b < c and b < d :
#     print (math.cos(b))
# elif c < a and c < b and c < d :
#     print (math.cos(c))
# elif d < a and d < c and d < b :
#     print (math.cos(d))


#####################################################################################

#6##
# import math
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))
# d = float(input('d: '))
# if a > b and a > c and a > d :
#     print (math.cos(a))
# elif b > a and b > c and b > d :
#     print (math.cos(b))
# elif c > a and c > b and c > d :
#     print (math.cos(c))
# elif d > a and d > c and d > b :
#     print (math.cos(d))

#####################################################################################

#7##
# a = [float(input('x1: ')), float(input('x2: ')), float(input('x3: '))]
# b = [float(input('y1: ')), float(input('y2: ')), float(input('y3: '))]
# pr_x1 = (a[0] + a[1] + a[2])/2
# pr_x2 = (b[0] + b[1] + b[2])/2
# S_x1 = pr_x1 * ((pr_x1 - a[0]) * (pr_x1 - a[1]) * (pr_x1 - a[2]))**0.5
# S_y1 = pr_x2 * ((pr_x2 - b[0]) * (pr_x2 - b[1]) * (pr_x2 - b[2]))**0.5
# if S_x1 == S_y1:
#     print ('S1=S2')
# else :
#     print('Foul!!!')

#####################################################################################

#8##
# a = [int(input('a: ')), int(input('osn: '))]
# p = (a[0] + a[0] + a[1])/2
# s = (p * (p - a[0]) * (p - a[0]) * (p - a[1]))**0.5
# if s % 2 == 0:
#     print ("S/2")
# else :
#     print("Не можу ділити на 2!")


#####################################################################################

#9##

# print(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
#        'December'][int(input()) - 1])

#####################################################################################

#10##
# from math import pi

# c = int(input('gradus 1 ,radian 2 '))
# b = float(input('b ='))
# if c == 1:

#     print(f"{b} radian = {b* 180 / pi} ")
# else:
#     print(f"{b} gradus ={ b * pi / 180}")

#####################################################################################

#11##
# a=3
# lista=[]
# i=0
# while i<a:
#     m=int(input("a,b,c"))
#     lista.append(m)
#     i+=1
# print(lista)
# count = 0

# for i in lista:
#     if i > 0:
#         count += 1
        
# print("Количество +: ", count)


#####################################################################################
#12##
# import math
# x=int(input())
# y=int(input())
# if x*y>0:
#    print(math.sqrt(x*y))
# else:
#    print((x+y)/2)

#####################################################################################

#13##
# import math
 
# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))
 
# mass = [x, y, z]
# gip = 0  
# p = 0  
# square = 0 
 

# if x > 0 and y > 0 and z > 0:
#     gip = max(s)  
#     mass.remove(gip)  
#     if gip ** 2 == mass[0] ** 2 + mass[1] ** 2:
#         p = (gip + mass[0] + mass[1]) / 2  
#         square = math.sqrt(p * (p - gip) * (p - mass[0]) * (p - mass[1]))
#         print(square)
#     else:
#         print('non')
# else:
#     print('non')

#####################################################################################

#14##
# a= int(input("a="))
# b= int(input("b="))
# c= int(input("c="))

# if (a < b + c) and (b < a + c) and (c < a + b):

#    p = (a+b+c)/2

#    s = (p*(p-a)*(p-b)*(p-c))**0.5

#    print(s)

# else:

#    print("трикутник існує")

#####################################################################################

#15##
# a = float(input('price= '))
# b = float(input('quan.= '))
# if b >= 100:
#     c = (a*b) * 0.9
#     print(f"sum={c}")
# else:
#     c = a*b
#     print(f"sum={c}")

#####################################################################################

#16##
# a = int(input('a=: '))
# b = int(input('b=: '))
# c = int(input('c=: '))
# if a == b == c:
#     print("Yes")
# else:
#     print("No")

#####################################################################################

#17##
# a = int(input('a= '))
# b = int(input('b= '))
# if (a**2 + b**2) > (a + b)**2:
#     print('(a**2 + b**2) > (a + b)**2')
# elif (a**2 + b**2) < (a + b)**2:
#     print('(a**2 + b**2) < (a + b)**2')

#####################################################################################

#18##
# a=3
# lista=[]
# i=0
# while i<a:
#     m=int(input("a,b,c"))
#     lista.append(m)
#     i+=1
# print(lista)



# for i in range(len(lista)):
#     if lista[i]>0:
#         print(lista[i]**2)

#####################################################################################


#19##
# R=int(input("Введите радиус:"))
# X=int(input("Введите X:"))
# Y=int(input("Введите Y:"))
# if X^2 + Y^2 < R:
#     print("Точка в круге")
# elif X^2 + Y^2 > R :
#     print("Точка вне круга")
# else:
#     print("Точка на окружности")

          
#####################################################################################

#20##
# import math
# a = float(input('Значение в радианах = '))
# if math.sin(a) > math.cos(a):
#     print('sin > cos')
# else:
#     print('cos > sin')

#####################################################################################

#21##
# def check(a,b,c):
#     sqa = pow(a, 2)
#     sqb = pow(b, 2)
#     sqc = pow(c, 2)
 
#     if (sqa == sqc + sqb or
#         sqb == sqa + sqc or
#         sqc == sqa + sqb):
#         print("Right-angled")
 
#     elif(sqa > sqc + sqb or
#             sqb > sqa + sqc or
#             sqc > sqa + sqb):
#         print("Obtuse-angled")
 
#     else:
#         print("Acute-angled")


# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))


# check(a, b, c)

#####################################################################################

#22##
# a = int(input('Enter side of the square: '))
# b = int(input('Enter radius of the circle: '))
# S_a = a**2
# S_b = 3.14*b**2
# if S_a > S_b:
#     print(' S square > circle')
# elif S_b > S_a:
#     print('S square < circle')

# elif S_b == S_a:
#     print('S square == circle')    

#####################################################################################

#23##

# a=3
# lista=[]
# i=0
# while i<a:
#     m=int(input("a,b,c"))
#     lista.append(m)
#     i+=1

# list_mask = []

# for item in lista:
#     if item > 0:
#         list_mask.append(item**3)
#     elif item < 0:
#         list_mask.append(0)
    

# print(lista)
# print(list_mask)

#####################################################################################

#24##
# a = int(input('x: '))
# b = int(input('y: '))
# if a > 0 and b > 0:
#     print('належить ')
# else:
#     print('He належить ')

#####################################################################################

#25##
# import math
# a =int(input("a="))
# b =int(input("b="))
# c =int(input("c="))
# print(math.fabs(a),math.fabs(b),math.fabs(c))

# print((a+b+c)/2)

#####################################################################################

#26##
# import math
# a = int(input("1= "))
# b = int(input("2= "))
# c = (a**2)-(b**2)
# c2 = math.fabs((a-b)**2)
# if c > c2:
#     print("Різниця квадратів більше.")
# else:
#     print("Модуль квадрата різниці більше.")


#####################################################################################

#27##
# a = int(input("a1= "))
# b = int(input("a2= "))
# c = int(input("a2= "))
# if a==b:
#     print("трикутник рівнобедр.")
# elif a==c:
#     print("трикутник рівнобедр.")
# elif c==b:
#     print("трикутник рівнобедр.")
# else:
#     print(" He рівнобедр.")

#####################################################################################

#28##
# a = int(input('x: '))
# b = int(input('y: '))
# if a < 0 and b > 0:
#     print('належить ')
# elif a > 0 and b < 0:
#     print('належить ')

# else:
#     print('He належить ')

#####################################################################################

#29##
# a = int(input("A= "))
# b = int(input("B= "))
# c = int(input("C= "))
# if a + b + c > 0:
#     print(2*(a + b + c))
# else:
#     print(0*(a + b + c))

#####################################################################################

#30##

# a=3
# lista=[]
# i=0
# while i<a:
#     m=int(input("a,b,c"))
#     lista.append(m)
#     i+=1

# list_mask = []

# for item in lista:
#     if item %2 !=0:
#         print(item)
    
    

