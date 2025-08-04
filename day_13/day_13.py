#day 13 of 30 days with python

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered= [i for i in numbers if i <= 0]
print (filtered)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_numbers = [item for sublist in list_of_lists for item in sublist]
print(list_of_numbers)

list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
countries_flat = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(countries_flat)

countries_flat1 = [{'country': country.upper(),'city': city.upper()} for [(country, city)] in countries]
print(countries_flat1)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
[('Donald', 'Trump')], [('Bill', 'Gates')]]
names_flat2 = [firstname + ' ' + lastname for [(firstname, lastname)] in names]
print(names_flat2)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
y_intercept = lambda m, x, y: y - m * x

m= slope(1, 2, 3, 4)
b = y_intercept(m, 1, 2)
print(f"Slope: {m}, Y-Intercept: {b}")