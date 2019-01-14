def gc_content(lst, lst_indx):
    count = []
    for i in lst:
        t=0
        for lett in i:
            if lett=='G':
                t += 1
            elif lett=='C':
                t += 1
            else:
                pass
        res = float(t * 100) / len(i)
        count.append(res)
        t=0
    result=max(count)
    idx=count.index(result)
    print(lst_indx[idx].replace('>',''))
    print(result)



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
    f = open('rosalind_gc.txt')
    lst = []
    lst_indx = []
    for name, seq in read_fasta(f):
        lst_indx.append(name)
        lst.append(seq)
    gc_content(lst, lst_indx)