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



def read_fasta(fp):
    name, seq = None, []

    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))




if __name__ == "__main__":
    fp = open('rosalind_pdst.txt')
    lst = []
    for name, seq in read_fasta(fp):
        lst.append(seq)
    pdst(lst, len(lst))