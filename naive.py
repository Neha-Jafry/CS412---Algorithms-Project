def naiveMatching(pat, txt):
    n = len(txt)
    m = len(pat)
    ind = []

    if m > n:
        print("Error: Given string length exceeds length of text to search in")

    else:
        for i in range(n - m + 1):
            found = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    found = False
                #  break
            if found:
                ind.append(i)
    return ind