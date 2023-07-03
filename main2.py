import collections
import copy
from typing import *

# input = [1, 2, 3]

# import copy
#
# a = "strawberry"
# b = "strawberry"
# c = 1
# d = 1
# e = copy.deepcopy(c)
#
#
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print()
#
# a = [[1,2],3]
# b = a
# c = a[:]
# d = a.copy()
# e = copy.deepcopy(a)
#
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print()
# print(id(a[0]))
# print(id(b[0]))
# print(id(c[0]))
# print(id(d[0]))
# print(id(e[0]))


input = [1, 2, 3]

def permute(nums: List[int]) -> List[List[int]]:
    length = len(nums)
    candidates = nums.copy()
    results = []

    def dfs(depth, path, candidates):
        if depth == length:
            results.append(path[:])
            return

        for candidate in candidates:
            copied_candidates = candidates[:]
            copied_candidates.remove(candidate)
            dfs(depth + 1, path + [candidate], copied_candidates)
    dfs(0, [], candidates)
    return results
print(permute(input))




def permute(nums: List[int]) -> List[List[int]]:
    length = len(nums)
    candidates = nums.copy()
    results = []

    def dfs(depth, path):
        if depth == length:
            results.append(path[:])
            return

        for i, num in enumerate(candidates):
            # if num not in path:
                candidates.pop(i)
                path.append(num)
                dfs(depth + 1, path)
                path.pop()
                candidates.insert(i,num)

    dfs(0, [])
    return results
print(permute(input))

def permute(nums: List[int]) -> List[List[int]]:
    results = []
    # path = []

    def dfs(depth, path):
        if depth == len(nums):
            results.append(path[:])
            return

        for num in nums:
            if num not in path:
                path.append(num)
                dfs(depth + 1, path)
                path.pop()

    dfs(0, [])
    return results
print(permute(input))

# def permute(nums: List[int]) -> List[List[int]]:
#     results = []
#
#     def dfs(depth, path):
#         if depth == len(nums):
#             results.append(path[:])
#             return
#
#         for num in nums:
#             if num not in path:
#                 dfs(depth + 1, path + [num])
#
#     dfs(0, [])
#     return results
# print(permute(input))



def combine(n: int, k: int) -> List[List[int]]:
    candidates = [num for num in range(1, n+1)]
    results = []
    # path = []
    # print(candidates)

    def dfs(depth, path, start):
        if len(path) == k:
            results.append(path[:])
            return
        for idx, candidate in enumerate(candidates[start:]):
            # if candidate not in path:
                path.append(candidate)
                dfs(depth+1, path, start+idx+1)
                path.pop()
    dfs(0, [], 0)
    return results

print(combine(4,2))


def combine(n: int, k: int) -> List[List[int]]:
    candidates = [num for num in range(1, n+1)]
    results = []
    path = []
    # print(candidates)

    def dfs(depth, path, candidates):
        if len(path) == k:
            results.append(path[:])
            return

        for index, candidate in enumerate(candidates):
            # if candidate not in path:
            path.append(candidate)
            dfs(depth+1, path, candidates[index+1:])
            path.pop()

    dfs(0, path, candidates)
    return results

print(combine(4,2))



def combine(n: int, k: int) -> List[List[int]]:
    candidates = [num for num in range(1, n+1)]
    results = []
    path = []
    # print(candidates)

    def dfs(depth, path, candidates):
        if len(path) == k:
            results.append(path[:])
            return

        for index, candidate in enumerate(candidates):
            # if candidate not in path:
                dfs(depth+1, path + [candidate], candidates[index+1:])

    dfs(0, path, candidates)
    return results

print(combine(4,2))


a = [i for i in range(1,10) if i % 2 == 0]

print(a)

b = (i for i in range(1,10) if i % 2 == 0)

print(*b)
