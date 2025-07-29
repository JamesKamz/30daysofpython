# day 7 of 30 days with pythyon challenge

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercice : level 1
print("Length of it_companies:", len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Snapchat', 'WhatsApp'])
print(it_companies)

it_companies.remove('Oracle')
print(it_companies)

#the diffence beetween remove and discard
it_companies.discard('Oracle')  # does not raise an error if 'Oracle' is not found  


#Exercices : Level 2
C = A.union(B)
print(C)

D = A.intersection(B)
print (D)

print("Is A subset of B?", A.issubset(B))

print('Are A and B disjoint sets?', A.isdisjoint(B))

# Join A with B and B with A
A.update(B)
B.update(A)
print("A after joining with B:", A)
print("B after joining with A:", B)

#the symetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference) 

del A, B, C, D  # delete the sets A, B, C, and D


#Exercics : level 3
age_set = set(age)
age_len= len(age)
age_list_len = len(age_set)

print ("Which lenght is bigger ?", age_len > age_list_len)

#Explain the difference between the following data types: string, list, tuple and set
print("String: A sequence of characters enclosed in quotes, immutable.")
print("List: An ordered collection of items that can contain duplicates, mutable.")
print("Tuple: An ordered collection of items that can contain duplicates, immutable.")
print("Set: An unordered collection of unique items, mutable.")
print("The difference between a list and a set is that a list can contain duplicate items and maintains order, while a set contains only unique items and does not maintain order.")

#I am a teacher and I love to inspire and teach people. How many unique
#words have been used in the sentence? Use the split methods and set to get
#the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print("Unique words in the sentence:", unique_words)
