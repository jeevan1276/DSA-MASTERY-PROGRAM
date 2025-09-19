class Solution(object):
    def maxProfit(self, prices):
        ans=0
        minprice=float('inf')
        for p in prices:
            minprice=min(minprice,p)
            ans=max(ans,p-minprice)
        return ans
