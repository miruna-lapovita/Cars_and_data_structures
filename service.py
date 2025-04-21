from filles import *
from entitateaMasina import *


class MasinaService:
    def __init__(self):
        self.lista_masini = citeste_masini_din_fisier("masini.txt") #ia masinile din lista din fisier cu citirea din filles

    def bubble_sort(self, lista, comparator):
        for i in range(len(lista)): #trece prin fiecare elemente
            for j in range(0, len(lista) - i - 1): #face algoritmul doar de la ultimul sortat
                if comparator(lista[j], lista[j + 1]) == 1: #daca priml e mai mare ca urmatorul
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] #le interschimba

    def merge_sort(self, lista, comparator):
        if len(lista) > 1: #cat timp lista are mai mult de un element
            mijloc = len(lista) // 2 #se taie in mijloc lista, adica gaseste elementul din mijloc
            stanga = lista[:mijloc] #lsiat din stanga mijlocului
            dreapta = lista[mijloc:] #lista din dreapta mijlocului
            self.merge_sort(stanga, comparator) #se cheama functia pentru fiecare jumatate de lista
            self.merge_sort(dreapta, comparator)
            i = j = k = 0
            while i < len(stanga) and j < len(dreapta): # cat indicii sunt intre stanga si dreapta
                if comparator(stanga[i], dreapta[j]) <= 0:
                    lista[k] = stanga[i] #comparare si interschimbare, il baga in lista noua, sortata
                    i += 1
                else:
                    lista[k] = dreapta[j]
                    j += 1
                k += 1 #trece la urmatorul indice din lista finala
            while i < len(stanga): #se ocupa de elementul ramas
                lista[k] = stanga[i]
                i += 1
                k += 1
            while j < len(dreapta):
                lista[k] = dreapta[j]
                j += 1
                k += 1

    def cautare_secventiala(self, criteriu_cautare): #efectiv ia la rand fiecare element si verifica
        for i, masina in enumerate(self.lista_masini):
            if criteriu_cautare in [masina.marca, masina.model, masina.token_masina]: #cauta in atributele obiectelor din clasa
                return i
        return None

    def cautare_binara(self, lista_sortata, criteriu_cautare): #functioneaza pe lista sortata
        stanga = 0
        dreapta = len(lista_sortata) - 1
        while stanga <= dreapta:
            mijloc = (stanga + dreapta) // 2
            if lista_sortata[mijloc].token_masina == criteriu_cautare:
                return mijloc
            elif lista_sortata[mijloc].token_masina < criteriu_cautare:
                stanga = mijloc + 1
            else:
                dreapta = mijloc - 1
        return None

    def sort_and_search(self, comanda):
        lista_sortata = self.lista_masini.copy()
        self.merge_sort(lista_sortata, lambda x, y: Masina.comparator(x.token_masina, y.token_masina))#sorteaza lista pentru cautare binara
        if comanda[0] == "SEARCH":
            criteriu = comanda[1]
            rezultat = self.cautare_binara(lista_sortata, criteriu)
            if rezultat is None:
                print("Nu s-a gasit nicio masina conform criteriului de cautare.")
            else:
                print(f"Masina gasita: {lista_sortata[rezultat].marca} {lista_sortata[rezultat].model}")

        elif comanda[0] == "SORT":
            criterii = comanda[1:]
            if not criterii:
                print("Criterii de sortare lipsa.")
            else:
                if criterii == ["tokenMasina"]:
                    self.bubble_sort(lista_sortata, lambda x, y: Masina.comparator(x.token_masina, y.token_masina))
                elif criterii == ["marca", "model"]:
                    self.bubble_sort(lista_sortata, lambda x, y: Masina.comparator((x.marca, x.model), (y.marca, y.model)))
                elif criterii == ["marca", "model", "tokenMasina"]:
                    self.merge_sort(lista_sortata, lambda x, y: Masina.comparator((x.marca, x.model, x.token_masina),
                                                         (y.marca, y.model, y.token_masina)))
                elif criterii == ["profit"]:
                    self.bubble_sort(lista_sortata, lambda x, y: Masina.comparator(x.profit, y.profit))
                else:
                    print("Criterii de sortare invalide.")

                scrie_masini_sortate_in_fisier(lista_sortata, "masini_sortate.txt")
                print("Masinile sortate au fost scrise in fisierul masini_sortate.txt.")

        else:
            print("Comanda invalida.")

    def test_search(self):
        lista_sortata = self.lista_masini.copy()
        rezultat = self.cautare_secventiala("rosv58slv")
#        assert rezultat == 46
        rezultat =  self.cautare_secventiala("yx6196wdcm")
#        assert rezultat == 15
        self.merge_sort(lista_sortata, lambda x, y : Masina.comparator(x.token_masina, y.token_masina))
        rezultat =  self.cautare_binara(lista_sortata, "fuvjx4hgj4")
#        assert rezultat == 24

    def test_sort(self):
        copie_lista = self.lista_masini.copy()
        assert copie_lista[0].marca == "Chevrolet"
        assert copie_lista[0].model == "Malibu"
        assert copie_lista[0].token_masina == "fuvjx4hgj4"
        assert copie_lista[0].pret_achizitie == 4236
        assert copie_lista[0].pret_vanzare == 4199
        self.merge_sort(copie_lista, lambda x, y : Masina.comparator(x.token_masina, y.token_masina))
        assert copie_lista[0].marca == "Subaru"
        assert copie_lista[0].model == "BRZ"
        assert copie_lista[0].token_masina == "0ibdu3n47t"
        assert copie_lista[0].pret_achizitie == 2987
        assert copie_lista[0].pret_vanzare == 3046
        self.bubble_sort(copie_lista, lambda x, y: Masina.comparator((x.marca, x.model), (y.marca, y.model)))
        assert copie_lista[0].marca == "Audi"
        assert copie_lista[0].model == "A3"
        assert copie_lista[0].token_masina == "wt98fnpsku"
        assert copie_lista[0].pret_achizitie == 3816
        assert copie_lista[0].pret_vanzare == 8993
        self.bubble_sort(copie_lista, lambda x, y: Masina.comparator((x.marca, x.model, x.token_masina), (y.marca, y.model, y.token_masina)))
        assert copie_lista[6].marca == "BMW"
        assert copie_lista[6].model == "3Series"
        assert copie_lista[6].token_masina == "61lxnbay0c"
        assert copie_lista[6].pret_achizitie == 6692
        assert copie_lista[6].pret_vanzare == 13222
        self.merge_sort(copie_lista, lambda x, y: Masina.comparator(x.profit, y.profit))
        assert copie_lista[0].marca == "Toyota"
        assert copie_lista[0].model == "Avalon"
        assert copie_lista[0].token_masina == "x8fu5lo3m9"
        assert copie_lista[0].pret_achizitie == 8920
        assert copie_lista[0].pret_vanzare == 3916