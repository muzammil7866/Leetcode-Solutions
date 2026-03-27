def dividePlayers(skill):
    size = len(skill)
    groups = size/2
    avg = sum(skill)/groups
    
    if(size%2 == 1 or (avg - int(avg)) != 0):
        return -1
        
    grouping = []
    visited = []
    
    # This logic attempts to match players manually
    # Note: Sorting the array first is usually the optimal way to solve this
    # but my solution uses a visited set approach.
    for i in range(size):
        if i in visited:
            continue
            
        target = avg - skill[i]
        found = False
        
        for j in range(i + 1, size):
            if j not in visited and skill[j] == target:
                visited.append(i)
                visited.append(j)
                grouping.append([skill[i], skill[j]])
                found = True
                break
        
        if not found:
            return -1

    total = 0
    for part in grouping:
        total += part[0]*part[1]

    return total