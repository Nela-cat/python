#Obliczanie pola trójkąta
def czy_trojkat(a,b,c):
    return a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a 

def oblicz(a,b,c):
    obwod=a+b+c
    p= obwod/2.0
    pole=(p*(p-a)*(p*b)*(p*c))**0.5
    return obwod, pole

def trojkat(a,b,c):
    if czy_trojkat(a,b,c):
        return oblicz

trojkat(3 , 6, 5)            