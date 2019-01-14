def reverse_complement_dna(a):
    b = ''
    r = []
    for letter in a:
        if letter == 'A':
            r.append('T')
        elif letter == 'T':
            r.append('A')
        elif letter == 'C':
            r.append('G')
        else:
            r.append('C')
    r.reverse()
    return b.join(r)

if __name__ == "__main__":
    f = open('rosalind_revc.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    a = ''.join(lst)
    print(reverse_complement_dna(a))