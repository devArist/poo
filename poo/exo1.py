class Voiture:
    caractere = 0
    def __init__(self, marque, couleur, vitesse):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse
        Voiture.caractere += 1

    def rouler(self) -> str:
        """Displays car's speed"""
        print(f'La vitesse maximal de cette {self.marque} est {self.vitesse}')

    def __str__(self):
        return f'Voici les caractéristiques de votre voiture:\nmarque: {self.marque}\ncouleur: {self.couleur}\nvitesse: {self.vitesse}'


v1 = Voiture('Peugeot', 'rouge', 14)
print(v1)