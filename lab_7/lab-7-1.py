import statistics
oc = int(input("Pod. il. ocen\n"))
lista1 =[]

i=0
while i<oc:
    m=int(input("Podaj oceny\n"))
    lista1.append(m)
    i+=1
print(lista1)
def oblicz_srednia():
    sr=statistics.mean(lista1)
    print(sr)

    lista1.append(sr)
    sort_lista1=sorted(lista1)
    print(sort_lista1)

oblicz_srednia()

f = lista1.pop(-1)
print(lista1)



