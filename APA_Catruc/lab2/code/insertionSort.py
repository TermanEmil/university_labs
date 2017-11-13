def insertionSort(tab, i = 0, j = 0):
	for i in range(1, len(tab)):
		j = i
		while j > 0:
			if tab[j] < tab[j - 1]:
				tab[j], tab[j - 1] = tab[j - 1], tab[j]
			j -= 1