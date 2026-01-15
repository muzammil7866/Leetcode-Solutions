def minLength(s):
    choice1 = 'AB'
    choice2 = 'CD'
    while(s.find(choice1) != -1 or s.find(choice2) != -1):
        s = s.replace(choice1, "")
        s = s.replace(choice2, "")
    return len(s)