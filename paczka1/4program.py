import baza

info1=baza.Filmy("kiler","Juliusz Machulski","Cezary Pazura","kiler:)")


info2=baza.Filmy("Czterej pancerni","Konrad Nałęcki","Janusz Gajos","szarik i czołg")


# Do sprawdzenia!!!!!!!!!!!!!!!!!!!!


info3=baza.Filmy.dodawanie(55) ######??????




# print(info1.reżyser)
# print(info2.title)
print(info1.title,info1.reżyser,info1.actor,info1.poster)
print(info2.title,info2.reżyser,info2.actor,info2.poster)