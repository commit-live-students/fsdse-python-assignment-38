from itertools import chain, combinations

def solution(a_list):
    """Enter code here"""
    return [list(z) for z in chain.from_iterable(combinations(a_list, r) for r in range(len(a_list)+1))]
