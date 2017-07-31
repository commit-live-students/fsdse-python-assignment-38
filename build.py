import itertools


def solution(a_list):
    a=[]
    for i in range(0,len(a_list)+1):
        for x in itertools.combinations(set(a_list),i):
            # print("iteration----"+str(i))
            a.append(list(x))
    return a
# help(itertools)
print(solution([10, 20, 30]))
# help(itertools.combinations)
