def pdst(lst,n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(len(lst)):
        for j in range(len(lst)):
                matrix[i][j] = hamming_distance(lst[i], lst[j])

    for row in matrix:
        print(' '.join(map(str,row)))

def hamming_distance(s,t):
    hd = 0
    n = 0
    for letter in s:
        lt = t[n]
        if not letter == lt:
            hd += 1
        n += 1
    hd1 = (float(hd)/len(s))
    if hd1 == .0:
        hd1 = int(hd1)
    return hd1

if __name__ == "__main__":
    large_dataset = open('rosalind_pdst (5).txt').readlines()
    lst = []
    for line in large_dataset:
        linee = line.replace('\n', '')
        lst.append(linee)
    new_lst = []
    for g in range(len(lst)):
        if g % 2 == 0:
            pass
        else:
            new_lst.append(lst[g])
    pdst(new_lst, len(new_lst))