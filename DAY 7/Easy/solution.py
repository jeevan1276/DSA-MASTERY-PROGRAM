class Solution:
    def largestPrimeFactor(self, n):
        while n % 2 == 0:
            n //= 2
        factor = 3
        max_prime = 2
        while factor * factor <= n:
            while n % factor == 0:
                max_prime = factor
                n //= factor
            factor += 2
        return max(n, max_prime)