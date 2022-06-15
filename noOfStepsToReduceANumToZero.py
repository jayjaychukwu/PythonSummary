class Solution():
    def numberOfSteps(self,num: int) -> int: 
        n = 0
        while num != 0:
            if num%2==0:
                num /= 2
            else:
                num -= 1
            n += 1
        return n

"""
Let's say the number is 8
1: 8/2 = 4
2: 4/2 = 2
3: 2/2 = 1
4: 1-1 = 0
Therefore it requires 4 steps to get to 0
"""

solution = Solution()
print(solution.numberOfSteps(8))
