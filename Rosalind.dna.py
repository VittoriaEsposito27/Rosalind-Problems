def dna_count(a):
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0
    for letter in a:
        if letter == 'A':
            count_A += 1
        elif letter == 'C':
            count_C += 1
        elif letter == 'G':
            count_G += 1
        else:
            count_T += 1
    print(str(count_A)+' '+str(count_C)+' '+str(count_G)+' '+str(count_T))


a = 'GATAAGCATATTTCATCGCGTCCGTTAATGGCCGGTTGAGCCGCCATTCCACCCCACCGAACCTAGATCTTTCATTAGCCAGCTCTGATAGTAGTAACCCACTCATTGATGATCCTACTATTAACCGACTGAGCCGAAGTTATAAACGCCTACGAGAGAGTACTCCTGAAGTGATGCCTATAAATATTTTAGATCAGTACGGCCTCAGTCGTAATTGTCGGCTCAAAGGGAGAGTTTTAGACCGGAGGTAACCTTATTAGAAGGGATGAAAGGTATATTAATATGGTACCGCACCGTCCGTACCGCGACAATCACGGCGGAGAACCTAATCGCTTATCAGCTGCACGGACTCCGACCATTCGTAATCCGATGCAATAACTGTAAGGTACTCGGAACGAGCCGGGATATACAAGCCAAAGCTGATTGCTATCCGGGACACCAAAGGCAAAAGCAGCCTAAACCGCGGCTTAACTGACAGTCTCCAACTCTAGCAATAGTACATCATGAAGGTGACGCGGCTGATGGGGAAAGCAATGATGCCCTCTGAACGATTACCACTAGTGACATCGGTGGGTACCTATAATGGGACGCTATTCGCACGAATGGACGACTTAAATGCTAGTAAGTGGCCTGGGGGGACGCTTCTTTACGCCGCTACAATCTCTCATGGCGTTGCGGTGCGCAAACCACGGTCCGCCGGTACCGCGCAAGTTAGCGTTTATCTTTACTCTAGACGCCAAGGATCTGCCGACTGATTCATCAAATACCACGGCGTGTGATTCCCATACAATATACCGTTGCTTGCCCGGGAACCTGTAAACATCGATTAACAATCTTGACAGTTAAGAAAGCGTCATCATTTGAGGGTTCCTACAGAAACTCATCAGCTTGTGAGTTAACCAGTTGAGTCTCTG'
print(dna_count(a))