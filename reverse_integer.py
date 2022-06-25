'''Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-231, 231 - 1], then return 0
'''


class Solution:
    def reverseInt(self, inputString):
        inputString = int(str(inputString)[::-1]) if inputString >= 0 else int("-"
                + str(inputString)[::-1][:-1])
        return -2 ** 31 <= inputString <= 2 ** 31 -1 and inputString or 0





if __name__ == '__main__':

#    inputInt = 123
    inputInt = -123
#    inputInt = 120
#    inputInt = 12345656799887

    objSolution = Solution()
    print(objSolution.reverseInt(inputInt))
