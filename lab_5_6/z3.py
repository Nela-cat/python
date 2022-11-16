#3
n = int(input("podaj długość tablicy:"))
list1=[]
i=0
while i <n:
    
    m= int(input("podaj licz. :"))
    list1.append(m)
    i+=1
    

print("list1", list1)   

ostatni = list1[-1]
print(ostatni)


new = list1[:-1]
print("new list: ", new)

su = 0 
su= sum(new)
print("sum", su)


print("ostaatni-sum", ostatni-su)