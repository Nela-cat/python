n = int(input("ile liczb:"))
list1=[]
i = 0 
while i < n :
    m = int(input("podaj licz. :"))
    list1.append(m)
    i+=1
print(list1)   
for i in list1:
    if i %5 ==0:
        list1.remove(i)
print(list1)        
