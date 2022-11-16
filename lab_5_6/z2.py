####################################
2
n = int(input("ile liczb:"))
list1=[]
i = 0 
while n <0:
    m = int(input("podaj liczby:"))
    list1.append(m)
    i+=1
print(list1)
for i in list1:
    if i <list1[len(list1)-1] :
        list1.remove(i)  
        print(list1)
        print("suma:", (sum(list1)))
        print("śr" , (sum(list1))/n)


#################################