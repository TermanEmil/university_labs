def quickSort(tab, firstI, lastI):
	iterations = 0
	if firstI < lastI:
		iterations += 1
		pi = _partition(tab, firstI, lastI)
		iterations += quickSort(tab, firstI, pi)
		iterations += quickSort(tab, pi + 1, lastI)
	return iterations

def _partition(tab, firstI, lastI):
	x = tab[firstI]
	i = firstI - 1
	j = lastI + 1

	while True:
		while True:
			j -= 1
			if tab[j] <= x: break
		while True:
			i += 1
			if tab[i] >= x: break

		if i < j:
			tab[i], tab[j] = tab[j], tab[i]
		else:
			return j
