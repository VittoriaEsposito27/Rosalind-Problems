import itertools


def perm(n):
    lst = []
    for a in range(1,n+1):
        lst += [a]
    permutations = list(itertools.permutations(lst))
    print(len(permutations))
    for permt in permutations:
        print(' '.join(map(str, permt)))


n = 7
perm(n)