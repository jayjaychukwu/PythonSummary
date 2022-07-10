"""
What is the ternary operator?
It allows testing a condition on a single line 
"""

# Syntax: [on_true] if [expression] else [on_false]

a, b = 10, 20

min = a if a < b else b

print(min)
# Output: 10

"""
There is a more direct way by using Dictionary, Tuples & lambda
"""
# With Tuple
x, y = 20, 40

# (if_check_is_false, if_check_is_true) [check]
print((y, x)[x > y])
# output: 40

# With Dictionary

print({True: x, False: y}[x > y])
# output: 40

# With lambda

f = lambda x: 1.1 * x if x > 100 else 1.05 * x

print(f(100))
# Output: 105.0
