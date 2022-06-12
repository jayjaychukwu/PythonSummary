def solution(A):
    A.sort()
    for a,b in enumerate(A, A[0]):
        if  a != b:
            if a not in A:
                if a>0:
                    return print(a)
                else:
                    while(a<=0):
                        a += 1
                    return a
if __name__ == "__main__":
    solution([4,2,1,5,9])

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