def reverseVowels(s):
    if(len(s) >= 1 and len(s) <= 3*(10**5)):
        positions = []

        # Identify positions of all vowels
        for i in range(len(s)):
            if(s[i] in 'aeiouAEIOU'):
                positions.append(i)

        # Reverse the list of positions to map last vowel to first position
        positions_reversed = positions[::-1]
        result = ""
        j = 0
        
        for i in range(len(s)):
            if(i not in positions):
                result = result + s[i]
            else:
                result = result + s[positions_reversed[j]]
                j = j+1

        return result