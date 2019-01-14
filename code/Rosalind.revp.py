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


def reverse_palindrome_pos(s):
    results = []
    for i in range(len(s)):
        for j in range(4,13):
            if i + j > len(s):
                continue
            s1 = s[i:i+j]
            s2 = reverse_complement_dna(s1)
            if s1 == s2:
                results.append((i + 1, j))
    return results


if __name__ == "__main__":
    f = open('rosalind_revp.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        if line.startswith('>'):
            pass
        else:
            lst.append(line)
    final_results = reverse_palindrome_pos(''.join(lst))
    print "\n".join([' '.join(map(str, r)) for r in final_results])
