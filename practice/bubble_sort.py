class Sort():
    def bubbleSort(self, inputArray : list) -> list:

        ArrayLength = len(inputArray)

        for c in range(ArrayLength - 1):
            for s in range(ArrayLength -c -1):

                if inputArray[s] < inputArray[s+1]: continue

                inputArray[s], inputArray[s+1] = inputArray[s+1], inputArray[s]

        return inputArray






if __name__ == '__main__':

    NumberArray = [3413243, 67433243, 2343, 53211, 124346, 234677, 309854]

    print(Sort().bubbleSort(NumberArray))
