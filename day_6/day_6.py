# Day 6 : 30 days of python

# an empty tuple
empty_tuple = ()


sisters = ('Yabo', 'Léa', 'Reine', 'Rachel', 'Nina')
brothers = ('Filbert', 'Abraham', 'Aimé')

# Join sisters and brothers tuples
siblings = sisters + brothers
print (siblings)

#how many siblings

print("Number of siblings:", len(siblings))

siblings_list = list(siblings)

parents = ('Georges', 'Rebecca')

family_members= siblings + parents
print("Family members:", family_members)

# level 2

*siblings, father, mother = family_members
print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'meat', 'fish', 'egg')

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

food_dtuff_tl= list(food_stuff_tp)
print("Food stuff list:", food_dtuff_tl)

#slice out the midle item from food_stuff_tp
middle_index = len(food_stuff_tp) // 2
middle_item = food_stuff_tp[middle_index]
print("Middle item:", middle_item)


#first three items and last three items from food_stuff_tl
first_three = food_dtuff_tl[:3]
last_three = food_dtuff_tl[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

#delete tuple
del food_stuff_tp

#check 
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway',
'Sweden')
print("Estonia is a nordic country:",  'Estonia' in nordic_countries)
print("Iceland is a nordic country:", 'Iceland' in nordic_countries)