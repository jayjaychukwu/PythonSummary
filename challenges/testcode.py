y = "stuff;thing;junk;"

z = y.split(";")
print(z)
# ['stuff', 'thing', 'junk', '']

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

letters = []

for letter in my_dictionary.values():
    letters.append(letter)

print(letters)


class A:
    def __init__(self):
        self.a = 0

    def change(self, n):
        self.a = n
        return self.a


obj = A()
obj.change(2)
print(obj.a)
