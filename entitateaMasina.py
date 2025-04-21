
#Constructorul clasei
class Masina:
    def __init__(self, marca, model, token_masina, pret_achizitie, pret_vanzare):
        self.marca = marca
        self.model = model
        self.token_masina = token_masina
        self.pret_achizitie = pret_achizitie
        self.pret_vanzare = pret_vanzare
        self.profit = self.pret_vanzare - pret_achizitie
#getters

    def get_marca(self):
        return self.marca

    def get_model(self):
        return self.model

    def get_token_masina(self):
        return self.token_masina

    def get_pret_achizitie(self):
        return self.pret_achizitie

    def get_pret_vanzare(self):
        return self.pret_vanzare

    def get_profit(self):
        return self.profit

    @staticmethod
    def comparator(car1, car2):
        if car1 < car2:
            return -1
        elif car1 > car2:
            return 1
        else:
            return 0

