
from collections import Counter

class Solution():
    def longestSubstring(self, inputString : str) -> int:
        
        answer = 0
        c = 0
        count = Counter()

        for idx, character in enumerate(inputString):
            
            count[character] += 1


            while count[character] > 1:

                count[inputString[c]] -= 1

                c += 1

            answer = max(answer, idx - c + 1)

        print(f' keys {count.keys()}')
        return answer













if __name__ == '__main__':


# answer = 3
#    stringInput = "abcabcbb"
# answer = 1
    stringInput = 'bbbbbb'

# answer = 3; pwke is a sequence and not a substring 'wke'
#    stringInput = "pwwkew"

    objSol = Solution()
    print(objSol.longestSubstring(stringInput))
