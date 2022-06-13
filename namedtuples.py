"""
namedtuples supports both access from key-value and iteration,
the functionality that dictionaries lack.
"""
#import namedtuple from collections module
from collections import namedtuple

#Declaring a namedtuple
Student = namedtuple('Student', ['name', 'age', 'DOB'])

#Adding values to the namedtuple
S = Student('Jay', '20', '291299')

#Accessing the namedtuple by index
print("The student is",S[1], "years old")

#Accessing using the placeholder declared
print("The student's name is : ", end="")
print(S.name)

#Accessing using the getattr() function
print("The DOB is : ", end='')
print(getattr(S, 'DOB'))

"""
Let's look at some Conversion techniques
"""
#using make() to return namedtuple from the iterable passed
#as an argument
li = ['Kelechi', '19', '040502']

print(Student._make(li))
#Result: Student(name='Kelechi', age='19', DOB='040502')

#using asdict() to return an OrderedDict
print(S._asdict())
#result: {'name': 'Jay', 'age': '20', 'DOB': '291299'}

#using ** op to return a namedtuple from a dictionary
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}
print(Student(**di))
#Result: Student(name='Nikhil', age=19, DOB='1391997')

"""
Let's look at extra operators
"""
#Display all the fields in the namedtuple
print(S._fields)
#Result: ('name', 'age', 'DOB')

#Returns a new namedtuple with a modified field value
print(S._replace(name='Kelly'))
#Result: Student(name='Kelly', age='20', DOB='291299')