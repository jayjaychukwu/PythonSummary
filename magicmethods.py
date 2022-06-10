class stringElement():

    #initializing the string
    def __init__(self, stringVar):
        self.stringVar = stringVar

    #This represents our object instead of printing just the memory location
    def __repr__(self):
        return 'object: {}'.format(self.stringVar)
        


#Driver code
if __name__ == '__main__':
    string = stringElement("Hello")

    print(string)