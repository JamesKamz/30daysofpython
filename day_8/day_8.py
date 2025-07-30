# Day 8 of 30 days with python
dog= {}

dog ['name'] = 'Rex'
dog ['color'] = 'black'
dog ['breed'] = 'Boxer'
dog['legs'] = '4'
dog ['age'] = '7'
print (dog)

student ={
    'first_name': 'James', 
    'last_name': 'Kamz', 
    'gender': 'male', 
    'age': 23, 
    'martital status': 'single', 
    'skills': ['SIEM', 'terminal', 'html', 'Javascript', 'bash'],
    'country':'Togo', 
    'city':'Lome',
    'address':'Agbalepedogan'}

print (len(student))

print(student['skills'])

student ['skills'].append('python') 
student ['skills'].append('hacking')
print(student)

student_keys= list(student.keys())
print(student_keys)

student_values = list(student.values())
print(student_values)

student_tp=student.items()
print (student_tp)

del student['age']
print(student)

del student