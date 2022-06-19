# Given a string, find the first non-repeating character in it and return its
# index
# If it doesn't exist, return -1. # Note: all the input strings are already
# lowercase


# Approach 1
def solution(c):
    frequency = {}
    for g in c:
        if g not in frequency:
            frequency[g] = 1
        else:
            frequency[g] += 1
    for g in range(len(c)):
        if frequency[c[g]] == 1:
            # modified to return char instead of the index
            return c[g]
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

print('###')

# Approach 2
import collections

def solution(c):
    # build hash map : character and how often it appears
    count = collections.Counter(c) # <-- gives back a dictionary with words occurence count
                                    # Counter({'1':1, 'e':3, 't':1, 'c':1,
                                    # 'o':1, 'd':1})

    # find the index
    # EDIT : modified to return the character instead of the idx
    for idx, ch in enumerate(c):
        if count[ch] == 1:
            return ch
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))
