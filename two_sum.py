# Rewriting two-sum.py myself

class GetSum():
    def twoSums(self, numbers : list[int], target : int) -> list[int]:

        numIndices = {}

        for idx, num in enumerate(numbers):
            print(f'{idx}, num {num}')
            if (target - num) in numIndices:
                return numIndices[target - num], idx
            numIndices[num] = idx
















if __name__ == '__main__':


    # Test Data
#    nums = [2,7,11,15]
#    target = 9
    numbers = [3,2,4]
    target = 6


    objGetSum = GetSum()

    print(objGetSum.twoSums(numbers, target))

