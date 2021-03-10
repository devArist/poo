class Personne:
    def __init__(self, nom, prenom, couleur, date_naissance):
        self._nom = nom
        self.prenom = prenom
        self.couleur = couleur
        self.date_naissance = date_naissance

    def se_deplacer(self):
        return 'En marchant'

    @property
    def age(self):
        return 2021 - self.__date_naissance

    @property
    def date_naissance(self):
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, annee):
        if annee < 2021:
            self.__date_naissance = annee
        else:
            raise Exception('Vous devez être né en dessous de 2021')

    def __str__(self):
        return f'{self._nom} {self.prenom}'


p = Personne('Irié', 'Aristide', 'noir', 1997)
p.date_naissance = 2021
print(f"{p} est né en {p.date_naissance} ")