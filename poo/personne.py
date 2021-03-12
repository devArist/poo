class Personne:
    def __init__(self, nom:str, sexe:str, adresses:list):
        self.__nom = nom
        self.__sexe = sexe
        self.__adresses = adresses
        if not(self.__sexe == 'M' or self.__sexe == 'F'):
            raise Exception('Input M or F for object sex')

    @property
    def nom(self):
        return self.__nom

    @property
    def sexe(self):
        return self.__sexe

    @property
    def adresses(self):
        return self.__adresses

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @sexe.setter
    def sexe(self, sexe):
        if not (sexe == 'M' or sexe == 'F'):
            raise Exception('Value of sex parameter must be M or F')
        self.__sexe = sexe

    @adresses.setter
    def adresses(self, adresses):
        self.__adresses = adresses


class ListePersonnes:
    def __init__(self, personnes:list):
        self.__personnes = personnes

    @property
    def personnes(self):
        return self.__personnes

    @personnes.setter
    def personnes(self, personnes):
        self.__personnes = personnes

    def find_by_nom(self, s:str):
        """
        Deternimes if name given
        in parameter exists
        or not into persons list
        """
        for personne in self.personnes:
            if personne.nom == s:
                return personne

    def exists_code_postal(self, cp:str) -> bool:
        for personne in self.personnes:
            for adresse in personne.adresses:
                return True
        return False

    def count_personne_ville(self, ville:str) -> int:
        counter = 0
        for personne in self.personnes:
            for adresse in personne.adresses:
                if adresse.ville == ville:
                    counter += 1
                    break
            continue

        return counter

    def edit_personne_nom(self, oldNom:str, newNom:str):
        for personne in self.personnes:
            if personne.nom == oldNom:
                personne.nom = newNom

    def edit_personne_ville(self, nom:str, newVille:str):
        for personne in self.personnes:
            for adresse in personne.adresses:
                if adresse.ville == nom:
                    adresse.ville = newVille