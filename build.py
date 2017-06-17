import itertools


def solution(a_list):
    comb = []
    a_list.sort()
    for i in range(len(a_list)+1):
        for j in itertools.combinations(a_list,i):
            comb.append(list(j))
    print list(comb)
    return comb

solution([10,20,30])
