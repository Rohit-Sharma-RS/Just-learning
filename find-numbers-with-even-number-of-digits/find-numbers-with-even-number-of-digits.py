class Solution(object):
    def findNumbers(self, nums):
        c=0
        n=0
        for i in nums:
            while(i>0):
                i=i/10
                c=c+1
            if(c%2==0):
                n=n+1
                c=0
            else:
                c=0
        return n