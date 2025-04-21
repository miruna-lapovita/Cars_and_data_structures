from service import MasinaService


class UserCommandLineInterface: #constructor ui
    def __init__(self, service):
        self.service = service

    def meniu(self): #printeaza meniu
        meniu = ""
        meniu = meniu + "Comenzi disponibile:\n"
        meniu = meniu + "SEARCH <criteriu>\n"
        meniu = meniu + "SORT <criteriu>\n"
        meniu = meniu + "EXIT\n"
        return meniu

    def run(self):
        while True:
            print(self.meniu())
            comanda = input("Introduceti comanda: ").split()# primeste comanda
            if comanda[0] == "EXIT":# iesire din progrem
                break
            self.service.sort_and_search(comanda)#daca nu e comanda exit, merge in sort sau in search
