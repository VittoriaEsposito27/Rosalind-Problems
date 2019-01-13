def gc_content(lst):
    count = []
    new_lst = []
    new_new_lst = []
    for g in range(len(lst)):
        if g % 2 == 0:
            new_new_lst.append(lst[g])
        else:
            new_lst.append(lst[g])
    for i in new_lst:
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
    print(new_new_lst[idx].replace('>',''))
    print(result)










if __name__ == "__main__":
    large_dataset = open('rosalind_gc.txt').readlines()
    lst = []
    for line in large_dataset:
        linee = line.replace('\n','')
        lst.append(linee)
    gc_content(lst)