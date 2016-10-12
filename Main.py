import Util
import sys

array1 = Util()
print("Please enter the array lenght:")
len = sys.stdin.readline()
array1.makeRandArray(len)
array1.sortArray()
array1.printSortedRandArray()