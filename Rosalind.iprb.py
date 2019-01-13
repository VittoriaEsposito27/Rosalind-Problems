def mendels_firstlaw(k, m, n):
    k, m, n = map(float,(k,m,n))
    pairs = [
        k * (k - 1),  # AA, AA pairs
        k * m,  # AA, Aa pairs
        k * n,  # AA, aa pairs
        m * k,  # Aa, AA pairs
        m * (m - 1) * 0.75, # Aa, Aa pairs
        m * n * 0.5, # Aa, aa pairs
        n * k,  # aa, AA pairs
        n * m * 0.5,  # aa, Aa pairs
        n * n * 0,  # aa, aa pairs
    ]
    tot_pop = k + m + n
    prob = sum(pairs) / (tot_pop * (tot_pop - 1))
    print(prob)


mendels_firstlaw(24,15,16)