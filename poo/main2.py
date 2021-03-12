from . import adresse, personne

print('Bienvenue dans mon programme de création de carnets d\'adresses')

name = input('Entrez votre nom complet: ')
gender  = None

while not(gender == 'M' or 'F'):
    print('Quel est votre sexe ? (M/F): ')

counter = int(input('Combien d\'adresses voulez-vous saisir: '))
for count in range(counter):
    street = input('Entrez la rue: ')
    town = input('Entrez la ville: ')
    