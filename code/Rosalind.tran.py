def tran(s,t):
    transt = 0
    transv = float(0)
    for nt in xrange(len(seq1)):
        if seq1[nt] == seq2[nt]:
            continue
        elif seq1[nt] == "A" and (seq2[nt] == "C" or seq2[nt] == "T"):
            transv += 1
        elif seq1[nt] == "G" and (seq2[nt] == "C" or seq2[nt] == "T"):
            transv += 1
        elif seq1[nt] == "C" and (seq2[nt] == "A" or seq2[nt] == "G"):
            transv += 1
        elif seq1[nt] == "T" and (seq2[nt] == "A" or seq2[nt] == "G"):
            transv += 1
        else:
            transt += 1
    ratio = transt / transv
    return ratio




if __name__ == "__main__":
    f = open('rosalind_tran.txt').readlines()
    lst = []
    s = []
    t = []
    for line in f:
        line = line.replace('\n', '')
        if line.startswith('>'):
            lst.append('none')
        else:
            lst.append(line)
    lst.remove(lst[0])
    e_index=lst.index('none')
    for element in lst[:e_index]:
        s.append(element)
    for element in lst[e_index+1:]:
        t.append(element)
    seq1 = ''.join(s)
    seq2 = ''.join(t)
    print(tran(seq1,seq2))