"""
Dunder or magic methods in Python are the methods having two prefix and suffix
underscores in the method name.
Dunder here means “Double Under (Underscores)”.
These are commonly used for operator overloading. 
These methods are the reason we can add two strings with '+' operator
without any explicit typecasting.

Here are examples below
"""
class stringElement():

    #initializing the string
    def __init__(self, stringVar):
        self.stringVar = stringVar

    #This represents our object instead of printing just the memory location
    def __repr__(self):
        return 'object: {}'.format(self.stringVar)

    #This allows you to add a string to the existing string
    def __add__(self, otherString):
        return self.stringVar + otherString

        


#Driver code
if __name__ == '__main__':
    string = stringElement("Hello")

    print(string + " Jay")

"""
Other dunder or Magic methods include __call__, __new__, __closure__, __len__
"""