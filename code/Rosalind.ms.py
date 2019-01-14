def merge_sort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k]=left[i]
                i=i+1
            else:
                lst[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            lst[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            lst[k]=right[j]
            j=j+1
            k=k+1


if __name__ == '__main__':
    f = open('rosalind_ms.txt').read()
    lst = list(map(int,f.rstrip().split()))
    merge_sort(lst)
    print(" ".join(str(x) for x in lst))


