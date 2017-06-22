import itertools


def solution(a_list):
    """Enter code here"""
    l = []
    for i in range(len(a_list)+1):
        for j in itertools.combinations(a_list,i):
            l.append(list(j))
    return l
