

oc = int(input("Pod. len\n"))
lista1 =[]
i=0

while i<oc:
    n = int(input("podaj wart. od 1 do 100"))

    lista1.append(n)
    i+=1
print()

def del_min(lista1):
    for del_min in range(2):


        lista1.pop(lista1.index(min(lista1)))
        
del_min(lista1)
print(lista1)

################################################################################
oc = int(input("Pod. len\n"))
lista2 =[]
i=0

while i<oc:
    n = int(input("podaj wart. od 1 do 100"))

    lista2.append(n)
    i+=1
print()

def del_max():
    for del_max in range(2):


        lista2.pop(lista2.index(max(lista2)))
        
del_max()
print(lista2)


############################################################################################
def g():
    for g in range(2):


        a= lista1.pop(lista1.index(min(lista1)))
        print("lista1 min",a)
        s= lista1.pop(lista1.index(max(lista1)))
        print("lista1 max",s)
        
       
       
g()

