class Solution(object):
    def isPalindrome(self, s):
        if s==' ':
            return True
        else:
            s1=''
            for i in s:
                i=i.lower()
                if i.isalnum()==True:
                    s1+=i
            if s1==s1[::-1]:
                return True
            else:
                return False
