def rabin_karp_search(pat, txt):
	n = len(txt)
	m = len(pat)
	ind = []
	base = 256
	# mod_prime = 151
	if m > n:
		print("Error: Given string length exceeds length of text to search in")

	else:
		pat_hash = 0
		txt_hash = 0

		for i in range(m):
			pat_hash =  ((pat_hash * base) + ord(pat[i]))
			txt_hash =  ((txt_hash * base) + ord(txt[i]))

		for i in range(n - m + 1):
			if pat_hash == txt_hash:
				found = True
				for j in range(m):
					if txt[i + j] != pat[j]:
						found = False
						break
				if found:
					ind.append(i)
			if i < n - m:
				leading = (ord(txt[i]) * (base ** (m - 1)))
				txt_hash = (base*(txt_hash - leading) + ord(txt[i + m]))
	return ind