def dna_into_rna(a):
    b=''
    r=[]
    for letter in a:
        if not letter == 'T':
            r.append(letter)
        else:
            r.append('U')
    return b.join(r)

if __name__ == "__main__":
    f = open('rosalind_rna.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    a = ''.join(lst)
    print(dna_into_rna(a))