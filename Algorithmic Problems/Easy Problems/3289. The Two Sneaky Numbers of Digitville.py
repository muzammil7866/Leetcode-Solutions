import numpy as np

def getSneakyNumbers(nums):
    final = []
    # Using numpy unique for unique elements (LeetCode supports pandas/numpy in specific environments)
    uniques = np.unique(nums)
    for num in uniques:
        if nums.count(num) == 2:
            final.append(num)
    return final