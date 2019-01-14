def bins(lst,arr):
    result=[]
    for i in lst:
        if i in arr:
            ind=arr.index(i)+1
            result.append(ind)
        else:
            result.append(-1)
    print(" ".join(str(x) for x in result))


if __name__ == '__main__':
    f = open('rosalind_rna.txt').read()
    x = map(int, f.split())
    y = map(int, f.split())
    arr = list(map(int,f.rstrip().split()))
    lst = list(map(int,f.rstrip().split()))
    bins(lst,arr)