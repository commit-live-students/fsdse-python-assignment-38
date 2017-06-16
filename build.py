import itertools


def solution(a_list):
    ans = []
    for i in range(0,len(a_list)+1):
        for j in (itertools.combinations(a_list,i)):
            ans.append(list(j))
    return ans
print solution([10,20,30])
