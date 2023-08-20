class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        mc=0
        for i in range(len(nums)):
            if(nums[i]==0):
                c=0
            else:
                c=c+1
                mc=max(mc,c)
        return mc