def gcdOfStrings(str1, str2):
    # Ensure str1 is the longer string
    if(len(str1) > len(str2)):
        longer = str1
        shorter = str2
    if(len(str2) > len(str1)):
        longer = str2
        shorter = str1

    if(len(str1) == len(str2) and str1 == str2):
        return str1
        
    if(len(str1) == len(str2) and str1 != str2):
        return ""

    # Check if doubling the shorter string matches the longer (base case check)
    check = shorter
    while(len(check) <= len(longer)):
        check = check*2
        if(check == longer):
            return shorter
        
    # Brute force reduction of the key string
    check = shorter
    while(len(check)!= 1):
        check = check[0:len(check)-1]
        
        if(len(longer)%len(check) == 0):
            quotient = int(len(longer)/len(check))
            temp = ""
            
            for i in range(0,quotient):
                temp = temp + check

            if(temp == longer):
                valid = True
                iterate = 0
                while(iterate < len(shorter)):
                    if(check != shorter[iterate: iterate + len(check)]):
                        valid = False
                    iterate = iterate + len(check)
                if(valid == True):
                    return check
            
    return ""