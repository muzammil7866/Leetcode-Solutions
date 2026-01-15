class Solution(object):
    def buildArray(self, nums):
        temp = []
        for i in range(len(nums)):
            temp.append(nums[nums[i]])
        return temp