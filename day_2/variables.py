#Jour2: 30 Days of Python Programming

# niveau 1
#defining variables
first_name="James"
last_name="Kamz"
full_name= first_name + " " + last_name
country="Togo"
city="Lome"
age=10
is_married=False
is_true=True
is_light_on=False

# multiple variable declaration
x, y, z = 5, 10, 15

# niveau 2
# Vérification du type de données de toutes les variables
print("Type de prénom:", type(first_name))
print("Type de nom de famille:", type(last_name))
print("Type de nom complet:", type(full_name))
print("Type de pays:", type(country))
print("Type de ville:", type(city))
print("Type d'âge:", type(age))
print("Type de est_marie:", type(is_married))
print("Type de is_true:", type(is_true))
print("Type de is_light_on:", type(is_light_on))

# Longueur du prénom
print("Longueur du prénom:", len(first_name))

# Comparaison de la longueur du prénom et du nom de famille
print("Prénom plus long que nom de famille ?", len(first_name) > len(last_name))

# Déclaration des variables numériques
num_one = 5
num_two = 4

# Opérations mathématiques
somme = num_one + num_two
difference = num_one - num_two
produit = num_one * num_two
division = num_one / num_two
reste = num_one % num_two
division_entiere = num_one // num_two

# Affichage des résultats
print("Somme:", somme)
print("Différence:", difference)
print("Produit:", produit)
print("Division:", division)
print("Reste (modulo):", reste)
print("Division entière (floor division):", division_entiere)

# calclul l'air et la circonference d'un cercle
from math import pi
radius_of_circle = 30
area_of_circle = pi * (radius_of_circle ** 2)
circumference_of_circle = 2 * pi * radius_of_circle
print("Aire du cercle:", area_of_circle)
print("Circonférence du cercle:", circumference_of_circle) 
radius_of_circle = input(int("Entrez le rayon du cercle: "))
area_of_circle = pi * (radius_of_circle ** 2)
print("Aire du cercle avec rayon entré:", area_of_circle)

# utiliser input pour avoir 
last_name = input("Entrez votre nom de famille: ")
first_name = input("Entrez votre prénom: ")
country = input("Entrez votre pays: ")
age = int(input("Entrez votre âge: "))

help ('keywords')