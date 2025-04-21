import time
import random
from service import MasinaService
from ui import UserCommandLineInterface
from filles import *


def generare_fisier_masini(n, nume_fisier):
    with open(nume_fisier, 'w') as file:
        for _ in range(n):
            marca = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5))
            model = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
            token_masina = ''.join(random.choices('0123456789', k=10))
            pret_achizitie = random.randint(1000, 50000)
            pret_vanzare = random.randint(pret_achizitie, 2 * pret_achizitie)
            file.write(f"{marca} {model} {token_masina} {pret_achizitie} {pret_vanzare}\n")


def testare_cautare(n, nume_fisier):
    # Inițializăm serviciul și citim datele din fișier
    service = MasinaService()
    # service.lista_masini = service.citeste_masini_din_fisier(nume_fisier)

    # Inițializăm lista de criterii de căutare pentru testare
    criterii_test = ["rosv58slv", "yx6196wdcm", "fuvjx4hgj4"]  # Exemple de token-uri de căutat

    total_time = 0.0
    for criteriu in criterii_test:
        start_time = time.time()
        service.cautare_binara(service.lista_masini, criteriu)
        end_time = time.time()
        total_time += end_time - start_time

    avg_time = total_time / len(criterii_test)
    print(f"Timpul mediu de căutare pentru n = {n}: {avg_time} secunde")


def main():
    nume_fisier = "masini.txt"
    # Generăm fișierele pentru diferite dimensiuni de date
    for n in [100, 1000, 5000]:
        generare_fisier_masini(n, nume_fisier)
        # Inițializăm serviciul și măsurăm timpul de execuție
        service = MasinaService()
        ui = UserCommandLineInterface(service)
        start_time = time.time()
        ui.run()
        end_time = time.time()
        print(f"Timpul de execuție pentru n = {n}: {end_time - start_time} secunde")