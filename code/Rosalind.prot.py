import re
import string
def translation(s):
    k = re.search('(AUG([ACGU]{3,3})+?)(UGA|UAA|UAG)', s)
    codons = re.findall(r'...', k.group(1))
    protein = ''
    genetic_code = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S',
                    'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'ACU': 'T',
                    'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'UAU': 'Y',
                    'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAG': 'Q', 'CAA': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAG': 'K',
                    'AAA': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
                    'CGU': 'R', 'CGA': 'R', 'CGG': 'R', 'CGC': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'AUG': 'M'}
    for codon in codons:
        for x in genetic_code:
            if codon == x:
                protein += genetic_code[x]
    return protein


if __name__ == "__main__":
    f = open('rosalind_prot.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    s = ''.join(lst)
    print(translation(s))