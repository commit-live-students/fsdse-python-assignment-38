import itertools

my_list = [10, 20, 30]

def solution(l):
    mainList = []
    for L in range(0,len(l)+1):
        for subset in itertools.combinations(l, L):
            mainList.append(list(subset))
    return (mainList)

solution(my_list)
