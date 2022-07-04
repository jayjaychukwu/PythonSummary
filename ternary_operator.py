"""
What is the ternary operator?
It allows testing a condition on a single line 
"""

#Syntax: [on_true] if [expression] else [on_false]

a, b = 10, 20

min = a if a < b else b

print(min)
#Output: 10