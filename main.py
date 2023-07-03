import collections
from typing import *


# Arrays implement the NumPy API
# import dask.array as da
# x = da.random.random(size=(10000, 10000),
#                      chunks=(1000, 1000))
# x + x.T - x.mean(axis=0)

def addition(n):
    return n+n
numbers = (1,2,3,4)

result = map(addition, numbers)
print(result)
print(type(result))
print(list(result))


strs: Deque = collections.deque()

s = '123'

print(s[5:7])


#
# s = ['2 A', '1 B', '4 C', '1 A']
# def func(x):
#     return x.split()[1], x.split()[0]
# # s.sort(key=func)
# # print(s.sort(key=func))
# c=sorted(s,key=func)
# print(c)
#


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(result)
print(list(result))


def addition2(n1, n2):
    return n1 + n2


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# result = map(lambda x,y:x+y, numbers1,numbers2)
result = map(addition2, numbers1, numbers2)
print(list(result))

a = [1, 2, 45]
print(enumerate(a))
print(list(enumerate(a)))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

a = [1, 2, 3, 4, 4]

b = collections.Counter(a)
b.most_common(2)
print(b)

import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print("The created heap is : ", (list(li)))
print("The created heap is : ", li)
print(type(li))

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5]
c = [3, 4, 5]
print(list(zip(a, b, c)))

nums = [1, 1, 1, 2, 2, 3]
k = 2

a = collections.Counter(nums).most_common(k)
print(a)
print(*a)
print(list(zip(a)))
print(list(zip(*a)))
print(nums)

fruits = ['a', 'b', 'c']
print(*fruits)
print(nums)
print(*nums)

import time

print(int(time.time()))

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(v: Any, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            recursive_dfs(w, discovered)


result = []
recursive_dfs(1, result)
print(f'recursive_dfs: {result}')
print(f'recursive_dfs: {recursive_dfs(2)}')
f'recursive_dfs: {recursive_dfs(3)}'


def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


result = iterative_dfs(1)
print(f'iterative_dfs: {result}')


def iterative_bfs(start_v):
    discovered = []
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                queue.append(w)
    return discovered


result = iterative_bfs(1)
print(f'iterative_bfs: {result}')


dic = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
result = []
digits = "23"
# def letterCombination(digits:str) -> List[str]:
def dfs(index, path):
    print("indfs")
    if len(path) == len(digits):
        result.append(path)
        return
    print("indfs")
    print(path)

    for char in dic[digits[index]]:
        dfs(index+1,path+char)
        print(path+char+"asdf")

dfs(0,"")
print(result)

