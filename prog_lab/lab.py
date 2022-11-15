# lab_1

# .2
# a1=int(input("podaj liczbe 1 : "))
# a2=int(input("podaj liczbe 2 : "))
# a3=int(input("podaj liczbe 3 : "))
# if a1 > a2 and a1 > a3:
#     print("liczba1: ", a1)
# elif a2> a1 and a2>a3:
#     print("liczba2:", a2  ) 
# else:
#     print("liczba3:", a3)       

# .3
# liczba = int(input("Podaj liczbe z zakresu 0 - 999. Twoja liczba: "))
# if liczba > 999 or liczba <0:
#     print("Podaj liczbe z zakresu 0 - 999")
# else :
#     print(f"Twoja liczba: {liczba}")    

# def suma(liczba):
#     s = 0
#     for i in str(liczba):
#         s += int(i)
#     return s
# def podzial(liczba):
#    setki = int(liczba/100%10)
#    dziesiatki = int(liczba/10%10)
#    jednosci = liczba%10
#    print(f"Setki: {setki}, dziesiątki: {dziesiatki}, jedności {jednosci}!")
# print(f"Suma cyft to: {suma(liczba)}")
# podzial(liczba)


#ROZDZIAŁ 3.
#2. Wczytać w pętli n liczb z przedziału od 10 do 50 (wartość n pobrać od użytkownika przed wejściem do pętli), a następnie wyświetlić sumę ich kwadratów.
# print("Podaj 3 liczby z przedziału od 10 do 50 : ")
# a1=int(input("a1="))
# a2=int(input("a2="))

# while a1 and a2 >10 and a1 and a2 < 50:
#     print(a1*a1 + a2*a2)
#     break

#3
#3. Wczytywać liczby od użytkownika do momentu, gdy ich suma przekroczy 255 lub iloczyn będzie większy od 50000, a następnie wyświetlić ich średnią arytmetyczną.
# srednia= 0
# a1=int(input("Podaj  liczbe 1: "))
# a2=int(input("Podaj  liczbe 2: "))
# suma=a1+a1
# while suma >225 and a1*a2 >50000 :
    
#     srednia=(a1+a1)/2
#     print(srednia)
#     break   

#4
# suma = 0
# parzystych = -1
# pobrana = 1
# while pobrana != 0:
#     pobrana= int(input('Podaj liczbe: '))

#     if pobrana % 2 == 0 or pobrana > 10: 
#         suma += pobrana 
#         parzystych += 1

# print('Liczb parzystych: ' + str(parzystych)) 
# print('Suma liczb parzystych: ' + str(suma))



  

# pobrana = 0
# while pobrana %2  == 0 :
#     pobrana= int(input('Podaj liczbe: '))
#     def suma(pobrana):
#         for i in str(pobrana):
#             print(i)
    
# def czy_trojkat(a, b, c):

#     return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b
# czy_trojkat(2, 3, 4)
        












# Napisz program wyświetlający palindrom, utworzony z danej liczby naturalnej n o dowolnej
# liczbie cyfr. Wydruk powinien mieć postać:
def isPalindrome(s):
    return s == s[::-1]
 
s = int(input("słowo:"))
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")