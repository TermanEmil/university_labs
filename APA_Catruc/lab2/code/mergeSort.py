def mergeSort(tab, firstI, lastI):
	if firstI < lastI:
		mid = int((firstI + lastI) / 2)

		mergeSort(tab, firstI, mid)
		mergeSort(tab, mid + 1, lastI)

		_merge(tab, firstI, mid, lastI)

def _merge(tab, firstI, mid, lastI):
	tmp = [0] * (lastI - firstI + 1)
	i = k = firstI
	j = mid + 1
	while i <= mid and j <= lastI:
		if tab[i] <= tab[j]:
			tmp[k - firstI] = tab[i]
			i += 1
		else:
			tmp[k - firstI] = tab[j]
			j += 1
		k += 1

	while i <= mid:
		tmp[k - firstI] = tab[i]
		k, i = k + 1, i + 1

	while j <= lastI:
		tmp[k - firstI] = tab[j]
		k, j = k + 1, j + 1

	#Copy tmp[] in tab[]
	for i in range(firstI, lastI + 1):
		tab[i] = tmp[i - firstI]