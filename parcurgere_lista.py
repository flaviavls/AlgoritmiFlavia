def parcurgere_lista():
    l = list()
    l = [100, 10, 200, 23, 134, 50, 40]
    print(l)
    for index in range(len(l)):
        print(l[index], end=",")

def parcurgere_lista1():
    l1 = list()
    l1 = [1, 2, 3, 4, 5]
    for element in l1:
        print(element) #sau
    for i in range(len(l1)):
        print(l1[i])

def lista_abc():
    l1 = list()
    a = 10
    b = 20
    c = 30
    l1 = [a+b+c]
    for element in l1:
        print(element)
    for i in range(len(l1)):
        print(l1[i])

def suma_litere():
    # definessc dictionarul/ hash table
    # sub forma de mai jos
    dic1 = {'a':10, 'b':20, 'c':30}
    suma = 0
    cu = "abc"
    for i in range (len(cu)):
        suma += dic1[cu[i]]
    print('Suma este:', suma)


if __name__ == "__main__":
    #parcurgere_lista()
    (parcurgere_lista1())