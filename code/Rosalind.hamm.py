def hamming_distance(s,t):
    hd = 0
    n = 0
    for letter in s:
        lt = t[n]
        if not letter == lt:
            hd += 1
        n += 1
    return hd


if __name__ == "__main__":
    f = open('rosalind_hamm.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    s = lst[0]
    t = lst[1]
    print(hamming_distance(s,t))
