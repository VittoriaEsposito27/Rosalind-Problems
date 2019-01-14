def lcs(s, t):
    result = []
    lengths = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                max(lengths[i+1][j], lengths[i][j+1])
    x, y = len(s), len(t)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            result = [s[x-1]] + result
            x -= 1
            y -= 1
    return ''.join(result)





if __name__ == "__main__":
    f = open('rosalind_lcsq.txt').readlines()
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
    new_s = ''.join(s)
    new_t = ''.join(t)
    print(lcs(new_s,new_t))


