
# zmienna1=lambda x,a,b: x+a+b+5
# print(zmienna1(3,4,6))

# lambda to wyrażenie i może być wpisywana w różne konstrukcje



lista=[1,2,3,4,5,6,7,8,9,10]
# lista2=[]
# for x in lista:
#     x+=1
#     lista2.append(x)
# print(lista2)


# cc=map(lambda x: x+1,lista)
# # print(cc)

# print(list(cc))



# #przykład gdzie lambda jest użyta jako argument

filtrowanie_listy=filter(lambda x: x>5, lista)
print(list(filtrowanie_listy))
