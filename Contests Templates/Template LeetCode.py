from collections import defaultdict as DD
from collections import OrderedDict 
from bisect import bisect_right
from heapq import heapify, heappush, heappop
from functools import lru_cache

import operator

alice = 'Alice'
bob = 'Bob'
# _T = 1
            
def pr(temp):
    print(temp)
def prnl(temp):
    for w in temp:
        pr(w)
# def q():
#     return input()
def ri():
    temp = int(input())
    return temp
def rl():
    temp = list(map(int,input().split()))
    return temp
def zipList(*args):
    return list(zip(*args))
def sml(temp, *indices):
    return sorted(temp, key = operator.itemgetter(*indices))
def getSlice(temp,index):
        return [temp[i][index] for i in range(len(temp))]
def swap(array,ind1,ind2):
        temp = array[ind1]
        array[ind1] = array[ind2]
        array[ind2] = temp
def kvFromDict(_d):
    return [(k,v) for k, v in _d.items()]
from math import comb
from math import gcd
def lcm(a, b):
    return abs(a*b) // gcd(a, b)
