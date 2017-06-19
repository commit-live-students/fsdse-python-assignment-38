import itertools


def solution(a_list):
    """Enter code here"""
    result =[]
    for i in range(0,len(a_list)+1):
           result.extend(list(itertools.combinations(a_list,i)))
    res = map(lambda x:list(x),result)
    return res
