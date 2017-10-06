import itertools
def solution(a_list):
    """Enter code here"""
    combs = []
    for i in range(0, len(a_list) + 1):
        combs.extend([list(x) for x in itertools.combinations(a_list,i)])
    return combs
