class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for i in nums:
            temp = i
            countless = 0
            countmore = 0
            
            # Count steps up
            while(temp%3 != 0):
                temp +=1
                if(temp%3 == 0):
                    countless+=1

            # Count steps down
            temp = i
            while(temp%3 != 0):
                temp -= 1
                if(temp%3 == 0):
                    countmore+=1
            
            count += min([countless, countmore])
        return count