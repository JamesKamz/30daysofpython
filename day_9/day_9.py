# Day 9 of 30 days with python

#Level 1
age = int(input("Enter your age: "))
if age >= 18 :
    print("You are old enough to drive.")
else:
    print("You are left with", 18 - age, "years to drive.")
    
my_age = 23
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print("I am", my_age - your_age, "years older than you.")
elif my_age < your_age:
    print("You are ", your_age - my_age, "years older than me.")
else:
    print("We are the same age.")
    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(b, "is greater than", a)
else:
    print("Both numbers are equal.")

# Level 2

score = int(input("Entrez le score de l'étudiant (0-100) : "))

# Vérification de la validité du score
if score < 0 or score > 100:
    print("Score invalide. Veuillez entrer une valeur entre 0 et 100.")
else:
    # Attribution du grade
    if 90 <= score <= 100:
        grade = 'A'
    elif 70 <= score <= 89:
        grade = 'B'
    elif 60 <= score <= 69 :
        grade = 'C'
    elif 50 <= score <= 59:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"La note de l'étudiant est : {grade}")

month = input("Enter month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month entered.")


fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(fruit)
    print(fruits)
    


#level 3

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB',
'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

#Check if the person dictionary has skills key, if so print
#out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    if len(skills) > 0:
        middle_index = len(skills) // 2
        print("Middle skill:", skills[middle_index])
    else:
        print("No skills available.")
        
#Check if the person dictionary has skills key, if so check
#if the person has 'Python' skill and print out the result.

if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.") 
        
''' If a person skills has only JavaScript and React, print('He
is a front end developer'), if the person skills has Node,
Python, MongoDB, print('He is a backend developer'), if the
person skills has React, Node and MongoDB, Print('He is a
fullstack developer'), else print('unknown title') - for more
accurate results more conditions can be nested!'''
skills = person['skills']
if 'skills' in person and skills == ['JavaScript', 'React'] :
    print("He is a front end developer")
elif 'skills' in person and skills == ['Node', 'Python', 'MongoDB']:
    print("He is a backend developer")
elif 'skills' in person and skills == ['React', 'Node', 'MongoDB']:
    print("He is a fullstack developer")
else:
    print("unknown title")   
    
    
#If the person is married and if he lives in Finland, print
#the information in the following format:
#Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print("The person is either not married or does not live in Finland.")