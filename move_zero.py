# Given an array nums, write a function to move all zeroes to the end of it
# while maintaining the relative order of non-zero element
#
# EDIT: modified to prepend
array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
tempList = []

def solution(nums):
    tempList.clear()
    for c in nums:
        print(f'c is {c}')
        if 0 in nums:
#        if c == 0:
            nums.remove(0)
#            nums.append(0)
            tempList[:0] = [0]
            nums = list(nums)
            print(f'tempList : {tempList}')
    return tempList + nums

print(f'nums {solution(array1)}')
print(f'nums {solution(array2)}')
