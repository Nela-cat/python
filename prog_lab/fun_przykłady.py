#Obliczanie pola trójkąta
# def czy_trojkat(a, b, c):

#     return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b
# def oblicz(a, b, c):
#     obwod = a + b + c
#     p = obwod / 2.0
#     pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(obwod, pole)
#     return obwod, pole
# def trojkat(a, b, c):
#     if czy_trojkat(a, b, c):
#         return oblicz(a, b, c)        
# trojkat(3, 4, 5)

#Napisać funkcję rekurencyjną nwd(a, b) wyznaczającą NWD(a, b) algorytmem Euklidesa.
# def nwd(a,b):
#     if (b == 0) :
#         return a

#     else:
#        return nwd(b,a%b)    

# a= nwd(39,27)    
# print(a)    


#Sprawdzenie poprawności liczby dni w miesiącu
# d = int(input('dzien = '))
# m = int(input('miesiac = '))
# r = int(input('rok = '))
# if m > 0 and m < 13 and r >= 1900:
#     if m == 4 or m == 6 or m == 9 or m == 11:
#         dni = 30
#     else:
#         dni = 31
#     if m == 2:
#         if (r % 4 == 0 and r % 100 != 0) or r % 400 == 0:
#             dni = 28
#         else:
#             dni = 29
#     if d >= 1 and d <= dni:
#         print('poprawna liczba dni: ', str(d) + '-' + str(m) + '-' + str(r))
#     else:
#         print('niepoprawna liczba dni, poprawny zakres od 1 do', dni)
# else:
#  print('niepoprawny miesiąc lub rok')

#Napisz funkcję wyświetlającą na ekranie cyfry dziesiętne wczytanej liczby naturalnej n
#począwszy od cyfry jedności. 
# pom = 325
# c1 = pom % 10
# pom = pom // 10
# c2 = pom % 10
# pom = pom // 10
# c3 = pom % 10
# print(c1,c2,c3)


#Palindrom Napisz program wyświetlający palindrom, utworzony z danej liczby naturalnej n o dowolnej
# liczbie cyfr. Wydruk powinien mieć postać:
#spraw
# def isPalindrome(s):
#     return s == s[::-1]
 
# s = input("słowo:")
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")
#roz
# def Palindrom(n):
#     a= str(n)[::-1]
#     b= str(int(n))+str(int(a))
#     print(b)

# Palindrom(1234)

#Napisz funkcję, która dla danego n wyświetli figurę z gwiazdek (wynik dla n = 4: **** )

# def gaf(n):
#     for i in range(n):
#         print('*' * n)
# gaf(4)        


# def liczby1(n):
#      for i in range(1, n):
#         for j in range(1, n):
#             print(i, end='')
#         print()
# liczby1(4)

#Napisz funkcję, która dla danego n zwróci n!

# def silnia(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     s = 1
#     for i in range(2, n + 1):
#         s = s * i
#         print(s)    
#     return s
# silnia(3)    

#Ciąg Fibonacciego – ciąg liczb naturalnych określony rekurencyjnie w sposób następujący:
# def Fibonacci(n):
   
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     elif n == 0:
#         return 0
 
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
# # Driver Program
# print(Fibonacci(3))
 

#Napisz funkcję, która wyświetli liczby całkowite od n do 1 oraz od 1 do n

# def fun(n):
#     if n == 1:
#         print(n, end=' ')
    
#     elif n<1:

#         print("non")
        
#     elif n>1:
#         fun(n-1)
#         print(n ,end='♡' )
       

# fun(7)

# #Napisz funkcję, która wyświetli liczby całkowite od 1 do n

# def druk2(n):
#     if n<1:
#         return None
#     elif n == 1:
#         print(n, end=' ')
#     else:
#         druk2(n-1)
#         print(n, end=' ')

# druk2(7)


# Napisz funkcję rekurencyjną wyświetlającą rozwinięcie binarne liczby naturalnej
# w odwrotnym i poprawnym porządku:
# Algorytm 1
# def bin(n):
#     if n<1:
#         print("bledne n")
#     elif n == 1:
#         print(1, end=" ")
#     else:
#         bin(n//2)
#         print(n % 2, end=" ")
# bin(5)        
# Algorytm 2
# def bin(n):
#     if n<1:
#         print("bledne n")
#     elif n == 1:
#         print(1, end=" ")
#     else:
#         print(n % 2, end=" ") 
#         bin(n//2)
# bin(5)        

##########################Funkcje – zakresy###################################################
# res=[]
# for el in list1:
#     res.append(sum(map(int,str(el))))
# print(res)    


#1
# tab = []
# m = int(input("m"))
# sum=0

# while m != 0 and m >-1:
#     tab.append(m)
#     m = int(input("m"))
# print(tab)

# a = len(tab)
# print(a)

# for i in tab:
#     sum += i
# print(sum)    

# sr= sum/a
# print(sr)

#1.2 nie dziawa
# tab = []
# m = int(input("m"))
# sum=0
# while True:
#     if m ==0 or m < -1:
#         break

#     tab.append(m)
#     m = int(input("m"))
#     print("tab" , tab)

#     a = len(tab)
#     print("len" , a)

#     for i in tab:
#         sum += i
#     print("sum" , sum)    

#     sr= sum/a
#     print("sr",sr)

#3

n = int(input("Podaj dlugość tablicy:")) 
list1 = [] 

i=0 
while i<n: 
    m=int(input("Poda liczba")) 
    list1.append(m) 
    i+=1 
    
print("list1:",list1)    
        
ostatni=list1[-1]
print("ostatni" , ostatni)

new=list1[:-1]
print("new",new)

sum = 0
for i in new:
    sum += i 
    print("sum" , sum)  
     

if sum >=ostatni:
     print("ostatni-sum=" , ostatni-sum)
else:
    print("ostatni>sum")       


# znalezionych=0
# k=0
# print(ostatni)
# while k<n:
#     liczba=list1[k]
#     suma=0
#     while liczba>0:
#         cyfra=liczba%10
#         suma=suma+cyfra
#         liczba=liczba/10
#         if suma>ostatni:
#             znalezionych+=1
#             [znalezionych]=list1[k]
#             k+=1
# print("znal:")     




          
 
 