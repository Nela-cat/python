oc = int(input("Pod. len\n"))
lista1 =[]
i=0

while i<oc:
    m=int(input("Podaj oceny\n"))
    lista1.append(m)
    i+=1
print(lista1)

def fun():
    suma=sum(lista1)
    print(f"suma: {suma}")
    pod=int(input("pod. el.\n"))
    lista1.append(pod)
    print(lista1)
    f = lista1.pop(-1)
    
    print(lista1)
    print(f"{f} wyd. el")
fun()        
