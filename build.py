import itertools


def solution(a_list):
    l_subset = [[]]
    for i in range(1, len(a_list)+1):
        for subset in itertools.combinations(a_list, i):
            lst = list(subset)
            l_subset.append(lst)
    return l_subset
