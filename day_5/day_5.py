# Day 5 of 30 days of python

list1= []
print(list1)

list2 = ['css', 'java', 'python', 'javascript', 'c', 'c++']
list2_length = len(list2)
print(list2_length)

# getting the first, the middle anb last item of the list

first_item = list2[0]
middle_item = list2[int(list2_length/2)]
last_item = list2[-1]

print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

mixed_data_types = ['james',23, 1,77, 'single', 'agp']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)

print("Length of mixed_data_types:", len(mixed_data_types))
print("Length of it_companies:", len(it_companies))

print ("First item of it_companies:", it_companies[0])
print ("Middle item of it_companies:", it_companies[int(len(it_companies)//2)])
print ("Last item of it_companies:", it_companies[-1])

it_companies[0] = 'Meta'
print("Updated it_companies:", it_companies)

it_companies.append('Tesla')
print("After appending Tesla:", it_companies)

it_companies.insert(4, 'Twitter')
print("After inserting Twitter at index 3:", it_companies)

it_companies [0] = it_companies[0].upper()
print("First company in uppercase:", it_companies)

joined='#; '.join(it_companies)
print(joined)

'Facebook' in it_companies
print("Is 'Facebook' in it_companies?", 'Facebook' in it_companies) 

it_companies.sort()
print("Sorted it_companies:", it_companies)

it_companies.reverse()
print("Reversed it_companies:", it_companies)

print("First 3 companies:", it_companies[:3])

print("First 3 companies:", it_companies[-3:])

# 20. Slice out the middle IT company/companies
length = len(it_companies)
if length % 2 == 0:
    middle = it_companies[length//2 - 1:length//2 + 1]
else:
    middle = [it_companies[length//2]]
print("Middle company/companies:", middle)


it_companies.pop(0)
print("After popping first company:", it_companies)

it_companies.pop(int(len(it_companies)/2))
print("After popping middle company:", it_companies)

it_companies.pop()
print("After popping last company:", it_companies)

it_companies.clear()
print("After clearing it_companies:", it_companies)

del it_companies
print("it_companies has been deleted.")

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined = front_end + back_end
print("Full stack technologies:", joined)

full_stack = joined.copy()

full_stack.append('Python')
full_stack.append('SQL')
print("Full stack with Python and SQL:", full_stack)    

# exercices 2 Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print("Sorted ages:", ages) 

min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages_length = len(ages)
len(ages)
print(ages[int(len(ages)/2-1)],ages[int(len(ages)/2)]) # 24,24

if ages_length % 2 == 0:
  cond1 = ages[ages_length//2]
  cond2 = ages[ages_length//2-1]
  median_age = (cond1 + cond2)/2

else: 
  median_age = ages[ages_length//2]
print(f'The median age of the ages is {median_age}')

average_age = sum(ages) / len(ages)
print("Average age:", average_age)  

# Find the range of the ages (max minus min)
rng = max(ages) - min(ages) # 7
print(f'The range of the ages is {rng}')
# Compare the value of (min - average) and (max - average), use abs() method 
abs(min(ages) - average_age) == abs(max(ages)- average_age) # not equal

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];


countries.sort()
countries_length = len(countries)

if countries_length % 2 == 0:
  cond1 = countries[countries_length//2]
  cond2 = countries[countries_length//2-1]
  middle_country = (cond1 , cond2)

else: 
  middle_country = countries[countries_length//2]
print(f'The mid country in the countries list is {middle_country}')

mid_country = countries[len(countries)//2]
print(f'The middle country in the list is {mid_country} ') # Lesotho
# confirming with index
countries.index('Lesotho') # index is 96 : correct. Lesotho is the 97th out of the 193 countries.

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_length = len(countries) # 193 = odd
first_half = countries[:countries_length//2]
second_half = countries[countries_length//2:]
first_half_length = len(first_half)
second_half_length = len(second_half)

print(f'The length of the two halves are {first_half_length} and {second_half_length} ')



# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
CH,RU,US,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic
print(f'The scandic countries in the last list given are {scandic}')