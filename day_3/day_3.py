# Exercices du Jour 3

from math import sqrt
from operator import le


age = 23
height = 1.76
comp = 1 +  2j

# un script qui invite l'utilisateur à entrer la base et la hauteur du triangle et calculer une zone de ce triangle (zone = 0,5 x b x h).
base = float(input("Entrez la base du triangle : "))
height = float(input("Entrez la hauteur du triangle : "))
area = 0.5 * base * height
print(f"La zone du triangle est : {area}")

# un script qui invite l'utilisateur à entrer le côté A, le côté B et l'angle C d'un triangle et calcule le périmètre du triangle (périmètre = A + B + C).

side_a = float(input("Entrez le côté A du triangle : "))
side_b = float(input("Entrez le côté B du triangle : "))
side_c= float(input("Entrez le côté C du triangle : "))
perimeter = side_a + side_b + side_c
print(f"Le périmètre du triangle est : {perimeter}")

# un script pour calculer la surface et périmètre d'un rectangle.
length = float(input("Entrez la longueur du rectangle : "))
width = float(input("Entrez la largeur du rectangle : "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"La surface du rectangle est : {area_rectangle}")

# un script pour calculer la zone et circonférence d'un cercle.
radius= float(input("Entrez le rayon du cercle : "))
pi=3,14
area_circle = pi * (radius ** 2)
circumference_circle = 2 * pi * radius
print(f"La zone du cercle est : {area_circle}")
print(f"La circonférence du cercle est : {circumference_circle}")

# un script pour calculer la pente, l'ordonnée X et l'ordonnée Y d'une ligne : y = mx + b
m = 2  
b = -2  

slope = m
y_intercept = (0, b)
x = -b / m
x_intercept = (x, 0)
print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)

# Slope is m= (y2 - 2y1) / (x2 - x1). Script pour calculer la pente et la distance entre deux points (2, 2) et (6, 10).
x1, y1 = 2, 2
x2, y2 = 6, 10
slope1 = (y2 - y1) / (x2 - x1)
distance= sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La pente entre les points ({x1}, {y1}) et ({x2}, {y2}) est : {slope1} et la distance est : {distance}")

#compare the slopes in tasks 8 and 9:
print(slope == slope1)
print(slope > slope1)
print(slope < slope1)
print(slope >= slope1)
print(slope <= slope1)
print(slope != slope1)

#un script pour calculer y = x² + 6x + 9 en entrant une valeur de x.
x_value = float(input("Entrez une valeur pour x : "))
y_value = x_value**2 + 6*x_value + 9
print(f"Pour x = {x_value}, y = {y_value}")

# Script pour trouver la longueur d'une chaîne de caractères.
lenght1=len("python")
lenght2=len("dragon")
print(lenght1>lenght2)

# using and operators
print("on is in python and dragon:", "on" in "python" and "on" in "dragon")

# using  in operator
print("Check if if jargon is in this sentence:", "jargon" in "I hope this course is not full of jargon")

#using not in operator
print("on is not in python and dragon:", "on" not in "python" and "on" not in "dragon")

# convertir un nombre entier en décimal et en chaines de caracteres
l = len("python")
decimal_number = float(l)
strin_l = str(decimal_number)
print(f"Le nombre entier {l} converti en décimal est : {decimal_number}")
print(f"Le nombre entier {l} converti en chaîne de caractères est : {strin_l}")

# comment savoir si un nombre est pair ou pas
number = int(input("Entrez un nombre entier : "))
print(f"Le nombre {number} est pair:", number % 2 == 0 )

# un script pour vérifier si la division entière de 7 par 3 est égale à 2.7
print("La division entière de 7 par 3 est égale à 2.7:", 7 // 3 == 2.7)

# verifier si le type de '10' est égal au type de 10
print("Le type de '10' est égal au type de 10:", type('10') == type(10))

# verifier si int('9.8') est égal à 10
print ("int('9.8') est égal à 10:", int(float('9.8')) == 10)

# un script qui permet de calculer le paiment d'une personne
hours = float(input("Entrez le nombre d'heures travaillées : "))
rate = float(input("Entrez le taux horaire : "))
payment = hours * rate
print(f"Le paiement pour {hours} heures à un taux de {rate} est :{payment}")

# un script qui affiche le nombre de secondes que tout le monde peut vivre tout le monde vit 100 ans
number_of_years= input(int("Entrez le nombre d'années : "  ))
number_of_years = 100
seconds_in_a_year = 60 * 60 * 24 * 365
total_seconds = number_of_years * seconds_in_a_year
print(f"Le nombre total de secondes dans {number_of_years} ans est : {total_seconds}")

# un script Python qui affiche le tableau suivant
#1 1 1 1 1 
#2 1 2 4 8 
#3 1 3 9 27 
#4 1 4 16 64 
#5 1 5 25 125

for i in range(1, 6):  # De 1 à 5
    print(f"#{i}", end=" ")
    for j in range(1, 5):  # 1, 2, 3, 4
        print(i ** (j - 1), end=" ")
    print() 
