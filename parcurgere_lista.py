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

def crypt_hash(propozitie):
    dict3crypt = {'a':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j',
                  'h':'k', 'i':'l', 'j':'m', 'k':'n', 'l':'o', 'm':'p', 'n':'q',
                  'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x',
                  'v':'y', 'w':'z', 'x':'a', 'y':'b', 'z':'c'}
    rezultat = ''
    for element in propozitie:
        if element in ('', ',', '-', '1','2', '3', '4', '5', '6', '7', '8', '9', '0', '?'):
            rezultat += dict3crypt[element]
        return rezultat


def decrypt_hash(propozitie):
    dict3crypt = {'d':'a', 'e':'b', 'f':'c', 'g':'d', 'h':'e', 'i':'f', 'j':'g', 'k':'h',
                  'l':'i', 'm':'j', 'n':'k', 'o':'l', 'p':'m', 'q':'n', 'r':'o', 's':'p',
                  't':'q', 'u':'r', 'v':'s', 'w':'t', 'x':'u', 'y':'v', 'z':'w', 'a':'x',
                  'b':'y', 'c':'x'}
    rezultat = ''
    for element in propozitie:
        if element in ('', ',', '-', '1','2', '3', '4', '5', '6', '7', '8', '9', '0', '?'):
            rezultat += element
        else:
            rezultat += dict3crypt[element]
    return rezultat



if __name__ == "__main__":
    #parcurgere_lista()
    (parcurgere_lista1())
    suma_litere()
    decrypt_hash()