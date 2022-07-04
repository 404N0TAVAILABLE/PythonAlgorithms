class Sort():
    def bubbleSort(self, array)-> list:

        for c in range(len(array) -1):
            for s in range(0, len(array) - c - 1):
                if (array[s] < array[s + 1]) : continue
                array[s], array[s+1] = array[s+1], array[s]

        return array



if __name__ == '__main__':
#    array = list(map(int, input("enter a list of numbers separated by spaces: ").split()))
    arrayInt = [121488,8774654,874874,8641,125448,59834943,2345]

    print(Sort().bubbleSort(arrayInt))
