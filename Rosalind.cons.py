def create_array(n,lstt):
    h = 4
    matrix = [[0 for x in range(n)] for y in range(h)]
    j_a = 0
    j_c = 1
    j_g = 2
    j_t = 3
    a = matrix[j_a]
    c = matrix[j_c]
    g = matrix[j_g]
    t = matrix[j_t]
    k=0
    for string in lstt:
        for char in string:
            if char == 'A':
                matrix[j_a][k] += 1
            elif char == 'C':
                matrix[j_c][k] += 1
            elif char == 'G':
                matrix[j_g][k] += 1
            else:
                matrix[j_t][k] += 1
            k += 1
        k = 0
    results = {'A': a,'C': c,'G': g,'T': t}
    print(consensus(results))
    print('A:'+' '+' '.join(map(str,a)))
    print('C:'+' '+' '.join(map(str,c)))
    print('G:'+' '+' '.join(map(str,g)))
    print('T:'+' '+' '.join(map(str,t)))


def consensus(profile):
    result = []

    keys = profile.keys()

    for i in range(len(profile[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = profile[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        result.append(max_k)

    return ''.join(result)




if __name__ == "__main__":
    large_dataset = open('rosalind_cons (1).txt').readlines()
    lst = []
    for line in large_dataset:
        linee = line.replace('\n','')
        lst.append(linee)
    new_lst = []
    for t in range(len(lst)):
        if t%2==0:
            pass
        else:
            new_lst.append(lst[t])
    n = len(new_lst[0])
    create_array(n,new_lst)
