def count_pos_sub(s,t):
    k= len(t)
    lst=[]
    j=0
    while k < len(s) and j < (len(s)-(len(t))):
        if t in s[j:k]:
          lst.append((j+1))
        j+=1
        k+=1
    return ' '.join(map(str,lst))



if __name__ == "__main__":
    f = open('rosalind_hamm.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    s = lst[0]
    t = lst[1]
    print(count_pos_sub(s,t))



