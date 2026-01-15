class Solution(object):
    def countBits(self, n):
        output = []
        for i in range(0,n+1):
            count = 0
            j = i
            # Standard method to count bits by dividing by 2
            while(j > 0):
                if(j%2 == 1):
                    count = count + 1
                j = j//2

            output.append(count)
        return output