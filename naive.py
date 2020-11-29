def naiveMatching(pat, txt): 
    n = len(txt) 
    m = len(pat) 
    ind = []

    for i in range(n - m + 1): 
        j = 0
        while(j < m): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
  
        if (j == m):  
            ind.append(i)
    return ind

print(naiveMatching('AABA','AABAACAADAABAABA'))

# O(m*(n-m))

