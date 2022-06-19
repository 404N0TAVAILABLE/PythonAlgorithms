# Given an array containing None vales fill in the None values with the most
# recent non Nonve value in the array

array1 = [1, None, 2, 3, None, None, 5, None]

def solution(nums):
    valid = 0
    res = []
    for c in nums:
        if c is not None:
            res.append(c)
            valid = c
        else:
            res.append(valid)
    return res

print(solution(array1))

