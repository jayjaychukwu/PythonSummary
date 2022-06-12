"""
The enumerate() method adds a counter to an iterable and 
returns it in the form of an enumerating object. It is used directly
for loops or can be converted into a list of tuples usng the list()
method.
"""
L1 = ['food', 'animal', 'property']

for ele in enumerate(L1):
    print(ele)
"""
(0, 'food')
(1, 'animal')
(2, 'property')
"""

for ele in enumerate(L1,100):
    print(ele)
"""
(100, 'food')
(101, 'animal')
(102, 'property')
"""

for count, ele in enumerate(L1):
    print(count)
    print(ele)
"""
0
food
1
animal
2
property
"""

college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))
"[(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]"