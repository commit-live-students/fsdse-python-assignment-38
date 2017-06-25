import itertools


def solution(a_list):
    """Enter code here"""
    sublist_of_list = []
    for i in range(0,len(a_list)+1):
        sublist_of_list += map(list,itertools.combinations(a_list,i))

    return sublist_of_list
    
