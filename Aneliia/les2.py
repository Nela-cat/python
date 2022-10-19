#import random
#user=input("Wybierz - papier, nożyce, kamien: ")
#possible_actions = ["papier","nożyce","kamien"]
#computer_action = random.choice(possible_actions)
#print(f"user: {user} computer:{computer_action}")
#if user==computer_action:
#    print(f"user==comp. {user}"  )

#elif user == "kamien":
#    if computer_action == "nożyce":
#        print("kamien > nożyce Wygrałeś!")
#    else:
#        print("papier > kamien nie Wygrałeś ).")
#elif user == "papier"  :
#    if computer_action=="kamien":
#        print("papier > kamien Wygrałeś!")
#    else:
#        print("papier < nożyce nie Wygrałeś ")   
#elif user=="nożyce" :
#    if computer_action == "papier":
#        print("papier < nożyce Wygrałeś!")
#    else:
#        print("nożyce <  kamien nie Wygrałeś ).")


#2
print("trzy dodatnie liczby")
licz1=int(input("licz1"))
licz2=int(input("licz2"))
licz3=int(input("licz3"))
if licz1>licz2 & licz1>licz3 :
    print(f"licz1:{licz1}")
elif licz2>licz3 & licz2>licz1 :
    print(f"licz2:{licz2}")
else:
    print(f"licz3:{licz3}")

    
      

