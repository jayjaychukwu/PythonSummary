"""
This is the equivalent of Switch case statements found in other languages.
"""

number = 5

match number:
    case 1:
        print("This is", number)
    case 5:
        print("I am the correct number,", number)
    case other:
        print("No match found")

# prints out "I am the correct number, 5"
# Note that this works on Python 3.10 and above
