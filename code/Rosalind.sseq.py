def sseq(s,t):
    c=[ ]
    for j in t:
        d=s.find(j)+1
        s=s[d:]
        if c==[ ]:
            c.append(d)
        else:
            c.append(d+c[-1])
    for y in c:
        print y,


if __name__ == "__main__":
    f = open('rosalind_sseq.txt').readlines()
    lst = []
    s=[]
    t=[]
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
    sseq(new_s,new_t)