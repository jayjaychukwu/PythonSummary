y = 'stuff;thing;junk;'

z = y.split(';')
print(z)
#['stuff', 'thing', 'junk', '']

my_dictionary = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
}

letters = []

for letter in my_dictionary.values():
    letters.append(letter)

print(letters)