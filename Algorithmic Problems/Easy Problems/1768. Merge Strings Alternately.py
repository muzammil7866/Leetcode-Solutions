class Solution(object):
    def mergeAlternately(self, word1, word2):
        smaller = 0

        if(len(word1) <= len(word2)):
            smaller = word1
            other = word2
        else:
            smaller = word2
            other = word1

        finalStr = ""

        # Alternating merge for the length of the shorter string
        for i in range(0, len(smaller)):
                finalStr += word1[i]
                finalStr += word2[i]

        # Append the remainder of the longer string
        for i in range(len(smaller), len(other)):
            finalStr += other[i]

        return finalStr