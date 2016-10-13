from Util import Array
import sys

array1 = Array()
print("Please enter the array lenght:")
len = sys.stdin.readline()
array1.makeRandArray(len)
array1.printRandArray()
array1.sortArray()
array1.printSortedRandArray()
