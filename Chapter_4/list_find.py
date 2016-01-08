def list_find(lst, target):
	index = 0
	while index < len(lst):
		if lst[index] == target:
			break
		index += 1
	else:
		index = -1
	return index
