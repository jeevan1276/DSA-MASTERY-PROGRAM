#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        s=str(n)
        k=len(s)
        n1=0
        for i in s:
            n1=n1+int(i)**k

        return n==n1                        