variabila = lambda x,y : x+y
print(variabila(6,4))

players = [{"prenume" : 'Ion',
            "nume" : 'Popescu',
            "varsta" : 32},
           {"prenume" : 'Silviu',
            "nume" : 'Marian',
            "varsta" : 12}]

sortare = sorted(players, key=lambda player : player ['varsta'])

print(sortare)

"""map"""

list1 = [1,5,6,7,8,9,11,2,3,56]
list3 = map(lambda x:x**2, list1)
print(list(list3))

"""zip"""

list_with_int = [1,2,3,4]
list_with_str = ('one','two','three','four','five')

result = zip(list_with_int,list_with_str)
print(list(result))

"""list comprehension"""

lista1 = [1,2,3,4,5,6,7]
lista2 = []
for i in lista1:
    lista2.append(i)

print(lista2)

lista2 = [i if i%2==0 else 0 for i in lista1]

print(lista2)

list3 = [x if x%2 ==0  and x%5==0 else 0 for x in range(50)]
print(list3)

dictionar = {}
for num in range(1,11):
    dictionar[num] = num*num

print(dictionar)

dict = {num: num*num for num in range(1,11) if num%2==0}
print(dict)