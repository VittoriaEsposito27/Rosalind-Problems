genetic_code = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S',
                    'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'CCU': 'P', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'ACU': 'T',
                    'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GCU': 'A', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'UAU': 'Y',
                    'UAC': 'Y', 'CAU': 'H', 'CAC': 'H', 'CAG': 'Q', 'CAA': 'Q', 'AAU': 'N', 'AAC': 'N', 'AAG': 'K',
                    'AAA': 'K', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W',
                    'CGU': 'R', 'CGA': 'R', 'CGG': 'R', 'CGC': 'R', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'AUG': 'M','UAA':'Stop','UAG':'Stop','UGA':'Stop'}

def reverse_complement_dna(s):
    q = ''
    r = []
    for letter in s:
        if letter == 'A':
            r.append('T')
        elif letter == 'T':
            r.append('A')
        elif letter == 'C':
            r.append('G')
        else:
            r.append('C')
    r.reverse()
    return q.join(r)


def dna_into_rna(s):
    q=''
    r=[]
    for letter in s:
        if not letter == 'T':
            r.append(letter)
        else:
            r.append('U')
    return q.join(r)



def translate_codon(codon):
    protein = None
    if len(codon) == 3 and genetic_code.has_key(codon):
        protein = genetic_code[codon]
    return protein



def possible_protein_strings(s):
    results = []
    indices = []

    l = len(s)
    for i in range(l):
        protein = translate_codon(s[i:i+3])
        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        found_stop = False
        protein_string = ''

        for j in range(i, l, 3):
            protein = translate_codon(s[j:j+3])

            if not protein:
                break

            if protein == 'Stop':
                found_stop = True
                break

            protein_string += protein

        if found_stop:
            results.append(protein_string)

    return results

if __name__ == "__main__":
    f = open('rosalind_hamm.txt').readlines()
    lst = []
    for line in f:
        line = line.replace('\n', '')
        lst.append(line)
    possible_a = possible_protein_strings(dna_into_rna(large_dataset))
    possible_b = possible_protein_strings(dna_into_rna(reverse_complement_dna(large_dataset)))
    print "\n".join(set(possible_a + possible_b))


