import random

class Array:

    def __init__(self):
        self.Array = []

    def makeRandArray(self,len):
        for ele in range(0,int(len)):
            self.Array.append(ele)

    def sortArray(self):
        b = 0
        a = 0
        end = len(self.rand_list)
        while end != 2:
            print(end)
            for ele in range (a + 1,end):
                if self.rand_list[ele] > self.rand_list[ele + 1]:
                    b = self.rand_list[ele]
                    self.rand_list[ele] = self.rand_list[ele + 1]
                    self.rand_list[ele + 1] = b
                else:
                    continue
            a = 0
            b = 0
            end -= 1

    def printSortedRandArray(self):
        print(self.Array)