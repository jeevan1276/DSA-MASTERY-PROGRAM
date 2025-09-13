import math

class Solution:
    def print_divisors(self, N):
        ans = set()
        for i in range(1, int(math.sqrt(N)) + 1):
            if N % i == 0:
                ans.add(i)
                ans.add(N // i)
        for divisor in sorted(ans):
            print(divisor, end=' ')