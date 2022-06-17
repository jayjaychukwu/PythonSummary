# def solution(A):
#     A.sort()
#     for a,b in enumerate(A, A[0]):
#         if  a != b:
#             if a not in A:
#                 if a>0:
#                     return print(a)
#                 else:
#                     while(a<=0):
#                         a += 1
#                     return print(a)
#         else:
#             while A[-1]>a+1:
#                 a += 1
#                 if a not in A:
#                     break
#             return print(a)
# if __name__ == "__main__":
#     solution([1,2,3])

"""
Test cases
Example test:   [1, 3, 6, 4, 1, 2]
OK

Example test:   [1, 2, 3]
Output (stderr):
Invalid result type, int expected, <class 'NoneType'> found.
RUNTIME ERROR (tested program terminated with exit code 1)

Example test:   [-1, -3]
OK

Detected some errors.
"""

l = [1,2,3]
def getMEX(a):
    found = False
    n = len(a)
    for i in range(1, n + 2):
        found = False
        for j in range(n):
            if a[j] == i:
                found = True
                break
        if found == False:
            return i

if __name__ == "__main__":
    print(getMEX(l))

#Going to try the hash method.