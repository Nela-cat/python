# import random
# while True:
#     user=input("Wybierz - papier, nożyce, kamien: ")
#     possible_actions = ["papier","nożyce","kamien"]
#     computer_action = random.choice(possible_actions)
#     print(f"user: {user} computer:{computer_action}")
#     if user ==computer_action:
#         print(f"user==comp. {user}")
#     elif user == "kamien":
#         if computer_action == "nożyce":
#             print("kamien > nożyce Wygrałeś!")
#         else:
#             print("papier > kamien nie Wygrałeś ).")   
#     elif user =="papier":
#         if computer_action=="kamien":
#             print("papier > kamien wygraLeś")
#         else:
#             print("papier < nożyce nie wygrałeś")    
#     elif user == "nożyce":
#         if computer_action == "papier":
#             print("papier < nożyce wygraełeś")
#         else :
#             print("nożyce <  kamien nie Wygrałeś ")    

#     play_again = ""
#     play_again = input("play again yes/no ?");

#     if play_again.lower() != "yes":
#         break
           

#3
# user_n1 = int(input("podaj liczbe 1 "))
# user_n2 = int(input("podaj liczbe 2 "))

# while True:
#     if user_n1 + user_n2 > 225 and user_n1 * user_n2 > 50000 :
#         print((user_n1 + user_n2 )%2)
#     elif user_n1 + user_n2 > 225 and user_n1 * user_n2 > 50000 :
#         user_n3 = int(input("podaj liczbe 3 "))
#         if user_n1 + user_n2 + user_n3 > 225 and user_n1 * user_n2 * user_n3> 50000 :
#             print((user_n1 + user_n2  + user_n3)%2)
#         else:
#             print("liczbe 1 + liczbe 2 + liczbe 3 < 225")    

#     u = "" 
#     u = input("play again yes/no ?")   
#     if u.lower() != "yes":
#         break     

# ile_gier = int(input('podaj liczbe kupionych gier:'))
# if ile_gier> 0 :
#     suma = 0 
#     licznik= 0 

#     while licznik < ile_gier:
#         cena = int(input('podaj cene kolejnej gry: '))
#         suma+= cena 
#         licznik +=1
#     srednia_cena = suma / ile_gier
#     print('srednia cena pojedynczej gry: ' + str(srednia_cena))    



# suma = 0 
# parzystych = 0 
# pobrana = 1 
# while pobrana !=0:
#     pobrana = int(input("podaj liczbe: "))

#     if pobrana % 2 == 0 or pobrana > 10 :
#         suma+= pobrana
#         parzystych += 1
# print('liczb parzystych: ' + str(parzystych))
# print('suma liczb parzystych:' + str(suma))         
   

#4
wartosc = 0

nie_parzystych = 0
pobrana = 1
while pobrana !=  2:
     pobrana = int(input("podaj liczbe: "))






