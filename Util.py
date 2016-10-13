import random

class Array:

    def __init__(self):
        self.array = []

    def makeRandArray(self,len):
        for ele in range(random.randrange(0,100)):
            self.array.append(ele)

    def sortArray(self):
        b = 0
        a = 0
        end = len(self.array)
        for end in range(end,1,-1):
            print(end)
            for ele in range(a,end-1):
                if self.array[ele] > self.array[ele + 1]:
                    b = self.array[ele]
                    self.array[ele] = self.array[ele + 1]
                    self.array[ele + 1] = b
                else:
                    continue
            a = 0
            b = 0

    def printRandArray(self):
        print("Start array: ",self.array)
            
    def printSortedRandArray(self):
        print(self.Array)
