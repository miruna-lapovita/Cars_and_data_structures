from entitateaMasina import Masina


def citeste_masini_din_fisier(nume_fisier):
    masini = []
    with open(nume_fisier, 'r') as file:
        for line in file:
            masina = line.strip().split()
            marca, model, token, pret_achizitie, pret_vanzare = masina
            masini.append(Masina(marca, model, token, int(pret_achizitie), int(pret_vanzare)))
    return masini


def scrie_masini_sortate_in_fisier(masini_sortate, nume_fisier):
    with open(nume_fisier, "w") as file:
        for masina in masini_sortate:
            file.write(f"{masina.get_marca()} {masina.get_model()} {masina.get_token_masina()} "
                       f"{masina.get_pret_achizitie()} {masina.get_pret_vanzare()}\n")
