import itertools


def perm(n):
    lst = []
    for a in range(1,n+1):
        lst += [a]
    permutations = list(itertools.permutations(lst))
    print(len(permutations))
    for permt in permutations:
        print(' '.join(map(str, permt)))


if __name__ == "__main__":
    f = open('rosalind_.txt').read()
    n = int(f)
    perm(n)