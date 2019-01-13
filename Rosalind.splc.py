import string
import re


def translation_with_splicing(s,intron0,intron1,intron2,intron3,intron4,intron5,intron6,intron7,intron8,intron9,intron10,intron11,intron12,intron13):
    exon = s.split(intron0)
    exons = str(exon[0] + exon[1])
    exon1 = exons.split(intron1)
    exons1 = str(exon1[0] + exon1[1])
    exon2 = exons1.split(intron2)
    exons2 = str(exon2[0] + exon2[1])
    exon3 = exons2.split(intron3)
    exons3 = str(exon3[0] + exon3[1])
    exon4= exons3.split(intron4)
    exons4=str(exon4[0]+exon4[1])
    exon5 = exons4.split(intron5)
    exons5 = str(exon5[0] + exon5[1])
    exon6 = exons5.split(intron6)
    exons6 = str(exon6[0] + exon6[1])
    exon7= exons6.split(intron7)
    exons7 = str(exon7[0] + exon7[1])
    exon8= exons7.split(intron8)
    exons8 = str(exon8[0] + exon8[1])
    exon9= exons8.split(intron9)
    exons9 = str(exon9[0] + exon9[1])
    exon10 = exons9.split(intron10)
    exons10 = str(exon10[0] + exon10[1])
    exon11 = exons10.split(intron11)
    exons11 = str(exon11[0] + exon11[1])
    exon12 = exons11.split(intron12)
    exons12 = str(exon12[0] + exon12[1])
    exon13 = exons12.split(intron13)
    exons13 = str(exon13[0] + exon13[1])
    mRNA1 = exons13.replace('T', 'U')
    k = re.search('(AUG([ACGU]{3,3})+?)(UGA|UAA|UAG)', mRNA1)
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


s='ATGATACTAGGCTTGCGACACCGTGGTCTGCAGGGGAGCGGTCAAGTCCAGGTTGCGTGAGACGAAAAGGAGAGTTGCCGCATGTGTCGTGTGTGTCAATGCTTGGGGACGGTATCAAGGCTGACCCAGACGCCAATATCCGCATCCATGCGTACTAAACAGGCGTATAGAGAGAATAAGACCCGGCTCAGATTCTGCGTTAGCGGACGATAGTATCTGCACAAGGTCAGGGCGACGTCCTCACGCGATTTCCGTTCACGACAATAGAATCCGCTCTTTCATAAATCGCGTTCGAGGGGAAATTCCCAGAAAGTTGAAACGACAGTACTAATACCGAGGTAGACCTCCGCGCGCCTTTCGACTCTACTCTACACGTCGCCAGTCGCGTAATTTATGAGGAATGTGCCACCGTCCACATCAGACCCTTAGTACCCTGTCTCGATAGGCTAACAAGAGAACCTTGCCCCCACAATTGCCCCAATCACCTCCAACGGGTATAGCAGTACGAGTGTCGTTCATGGAGTTGGGAAATCGCGTTTCGTGCGGTACCTTAGGGGTTCGTAGGTTACTCGTACCCAATCCCGCGCAACACGGCTGTACCTGCGGATATCTTTTTGCTAATCGGGCAATACGATACGAAAAGCCGTTATTCTTCCAGCATATCAGGTGCATAGAGGTTGAACCGACCTACACGCATTCAGGCTGCCCAGGGTATCGACCCCGCGGTCCGCCACTGGACTTCCCGGGAAGGCCAATTTACTACCCATAGGAACAGATCCAGTAGTACGATATACGGACAATACGGACTTCCTCTGGCGCTTGACCACCGTTGTTCAGCACCCTATCTGCTAAATCCGTGCGTCGGTCGTCATTCGAAAAGTTACCGATCGGTCCGGTTGGGCAGCTGCAGAACGAACCTATATGCATCAATCAAAGCGTGTAGACTTCAATGCCAGCTTTACTCTGACTGACGATTCGGCTAGAGGATTTTGA'
intron0='AAATCGCGTTTCGTGCGGTACCTTAGGG'
intron1='TATCTGCTAAATCCGTGCGTCGGTCGTCATTCGAAAAGTTACCGAT'
intron2='CTTTTTGCTAATCGGGCAATACGATAC'
intron3='AGTAGTACGATATACGGACAATACGGACTT'
intron4='GTTCACGACAATAGAATCCGCTCTTTCATAAATCGCGTTCG'
intron5='TAGACCTCCGCGCGCCTTTCGACTCTACTCTACACGTCGCCAGTCGCGTA'
intron6='TGTCTCGATAGGCTAACAAGAGAA'
intron7='TTCCAGCATATCAGGTGCATAGAGGTTGAACC'
intron8='GCCACTGGACTTCCCGG'
intron9='GCGTGAGACGAAAAGGAGAGTTGCCGCATGTGTC'
intron10='CTCCAACGGGTATAGCAGTACGAGT'
intron11='GGCTCAGATTCTGCGTTAGCGGAC'
intron12='CATCAATCAAAGCGTGTAGACTTCAATGCCAGCTTTACTCTG'
intron13='CGGTATCAAGGCTGACCCAGACGCCAATATCCGCAT'
print(translation_with_splicing(s,intron0,intron1,intron2,intron3,intron4,intron5,intron6,intron7,intron8,intron9,intron10,intron11,intron12,intron13))
