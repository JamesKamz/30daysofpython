# Exercices du Jour 3

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
slope = (y2 - y1) / (x2 - x1)
