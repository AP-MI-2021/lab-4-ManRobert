def citire():
    lista = []
    numar_elemente = int(input("Dati numarul elementelor "))
    for i in range(numar_elemente):
        lista.append(int(input("Dati elementul cu numarul " + str(i+1) + " ")))
    return lista


def meniu():

    print("1. Citeste datele / Citeste alte date ")
    print("2. Afișarea listei după eliminarea numerelor prime din listă ")
    print("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat. ")
    print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului ")
    print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe ")
    print("prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia ")
    print("poziție apare numărul de apariții a numărului.")
    print("6. Iesire")


def is_prim(element):
    """
    Functia verifica daca un element este nr prim
    :param element: numar intreg
    :return: True daca este prim, False daca nu este prim
    """

    if element < 0:
        element = element * -1

    if element < 2:
        return False
    i = 2
    while i * i <= element:
        if element % i == 0:
            return False
        i += 1
    return True


def eliminare_nr_prime(lista):
    """
    Functia construieste o noua lista in care nu exista elemente prime
    :param lista: lista de numere intregi
    :return: lista fara elemente prime
    """
    lista_returnata = []
    for element in lista:
        if is_prim(element) == False:
            lista_returnata.append(element)
    return lista_returnata


def test_eliminare_nr_prime():
    assert eliminare_nr_prime([1, 2, 3, 4]) == [1, 4]
    assert eliminare_nr_prime([-1, -2, 5, 6]) == [-1, 6]
    assert eliminare_nr_prime([]) == []


def media_mai_mare_decat_n(lista, n):
    """
    Functia calculeaza media aritmetica a elementelor listei,si verifica daca aceasta
    este mai mare decat un numar n dat
    :param lista: lista de numere intregi
    :param n: numar intreg
    :return:Da daca media este mai mare decat n, Nu daca nu este
    """

    suma = 0
    for element in lista:
        suma = suma + element
    media = 0
    if len(lista) > 0:
        media = suma / len(lista)
    if media > n:
        return "Da"
    else:
        return "Nu"


def test_media_mai_mare_decat_n():
    assert media_mai_mare_decat_n([10, -3, 25, -1, 3, 25, 18], 10) == "Da"
    assert media_mai_mare_decat_n([1, 1, 1], 20) == "Nu"
    assert media_mai_mare_decat_n([], 1) == "Nu"


def determinare_nr_divizori(element):
    """
    Determina numarul de divizori proprii al unui element
    :param element: numar intreg
    :return: numarul divizorilor ( numar natural >= 0)
    """

    numar_divizori = 0
    for i in range(2, int(element/2) + 1):
        if element % i == 0:
            numar_divizori = numar_divizori + 1
    return numar_divizori


def adaugare_divizori_proprii(lista):
    """
    Functia creeaza o noua lista in care,dupa fiecare element din
    lista originala se adauaga nr de divizori proprii ai elementului curent
    :param lista:lista de numere intregi
    :return: lista noua cu elemente adaugate(daca este cazul)
    """
    lista_noua = []
    for element in lista:
        lista_noua.append(element)
        lista_noua.append(determinare_nr_divizori(element))
    return lista_noua


def test_adaugare_divizori_proprii():
    assert adaugare_divizori_proprii([2, 3, 4, 5]) == [2, 0, 3, 0, 4, 1, 5, 0]
    assert adaugare_divizori_proprii([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert adaugare_divizori_proprii([]) == []


def numarare_aparitii(element, lista):
    """
    Functia retunreaza nr de aparitii ale elementului in lista
    :param element: numar intreg
    :param lista: lista de numere intregi
    :return: numarul aparitiilor
    """

    numar = 0
    for i in lista:
        if element == i:
            numar = numar + 1
    return numar


def determinare_tuplu(lista, pozitie, element):
    """
    Functia returneaza tuplul format din element, pozitia acestuia, si numarul aparitiilor
    :param lista: lista de numere intregi
    :param pozitie: numar natural
    :param element: numar intreg
    :return: tuplul de numere (format din nr, indicele elementului, si numarul aparitiilor)
    """
    numar_aparitii = numarare_aparitii(element, lista)
    return element, pozitie, numar_aparitii


def inlocuire_cu_un_tuplu(lista):
    """
    Functia inlocuieste elementele cu un tuplu format din:
    elementul in sine, pozitia acestuia in lista, si numarul aparitiilor acestuia in lista
    :param lista: lista de numere intregi
    :return: noua lista cu elementele tuplu
    """

    lista_noua = []
    for i in range(len(lista)):
        lista_noua.append(determinare_tuplu(lista, i, lista[i]))
    return lista_noua


def test_inlocuire_cu_un_tuplu():
    assert inlocuire_cu_un_tuplu([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert inlocuire_cu_un_tuplu([]) == []
    assert inlocuire_cu_un_tuplu([1, -1, 2]) == [(1, 0, 1), (-1, 1, 1), (2, 2, 1)]


def teste():
    test_eliminare_nr_prime()
    test_media_mai_mare_decat_n()
    test_adaugare_divizori_proprii()
    test_inlocuire_cu_un_tuplu()


def main():
    lista = []
    lista_afisata = []

    teste()
    print("Programul a trecut testele de baza ")

    while True:
        print("Momentan,elementele citite sunt: " + str(lista))
        meniu()
        optiune = int(input("Dati optiunea "))
        if optiune == 1:
            lista = citire()
            print("Ati citit un set de date ")
        elif optiune == 2:
            lista_afisata = eliminare_nr_prime(lista)
            print("Noua lista este : " + str(lista_afisata))
        elif optiune == 3:
            numar_citit = int(input("Dati numarul "))
            afisare = media_mai_mare_decat_n(lista, numar_citit)
            print("Raspunsul este " + afisare)
        elif optiune == 4:
            lista_afisata = adaugare_divizori_proprii(lista)
            print("Noua lista este: " + str(lista_afisata))
        elif optiune == 5:
            lista_afisata = inlocuire_cu_un_tuplu(lista)
            print("Lista in urma operatiunilor este: " + str(lista_afisata))
        elif optiune == 6:
            print("La revedere ")
            break
        else:
            print("Optiune gresita, alegeti din nou ")


if __name__ == '__main__':
    main()
