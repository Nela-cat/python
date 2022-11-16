#######################################
#4

n = int(input("ile liczb:"))
list1=[]
i = 0 
while i < n :
    m = int(input("podaj licz. :"))
    list1.append(m)
    i+=1
print(list1)   
for i in list1:
    if i %2 ==0:
        list1.sort(key=lambda i:( i%2, not i%2)) 

print(list1)
