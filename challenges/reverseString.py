#solution1
def solution1(string):
        reverseString = list(string)
        reverseString.reverse()
        newreverseString = ''.join(i for i in reverseString)
        return newreverseString

#Simpler solution
def solution2(str):
  return str[::-1]

if __name__ == "__main__":
    print(solution1('world'))
    print(solution2('help'))
