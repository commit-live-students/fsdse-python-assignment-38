import itertools
def solution(a_list):
    x=[]
    for n in range(len(a_list)+1):
        for i in itertools.combinations(a_list, n):
            x.append(list(i))
    return x
