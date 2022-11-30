# class Czlowiek():
#     pass
    
# obiekt1=Czlowiek()
# obiekt1.imię="Tomasz"
# obiekt1.nazwisko="Kowalski"
# obiekt1.wiek=23
# obiekt1.wzrost=176
# obiekt1.pesel=92323134543
# obiekt1.nrUbezpieczenia=44444

# obiekt2=Czlowiek()
# obiekt2.imię="Romek"
# obiekt2.nazwisko="Nowak"
# obiekt2.wiek=33
# obiekt2.wzrost=192
# obiekt2.pesel=87121487463
# obiekt2.nrUbezpieczenia=555555



# print(obiekt2.nazwisko)
# print(obiekt2.wiek)



class Człowiek():
    def __init__(self,imię,nazwisko,wiek,wzrost,pesel,nrUbezpieczenia):
        self.imię=imię
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.wzrost=wzrost
        self.pesel=pesel
        self.nrUbezpieczenia=nrUbezpieczenia

    def dodawanie(self,a):
        print(a)




obiekt3=Człowiek("Ola","Iksińska",44,154,432123456,333333)
obiekt4=Człowiek("Janek","Beksiński",33,184,3453423232,44444)

obiekt3.dodawanie("s")

print(obiekt3.wiek)
# print(obiekt3.nazwisko)