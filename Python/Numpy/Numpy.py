# Q = https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true


import numpy as np

a = np.array(input().split(),dtype =int)
b = np.array(input().split(),dtype= int)


arr1 = np.inner(a,b)
print(arr1)

arr2 = np.outer(a,b)
print(arr2)
