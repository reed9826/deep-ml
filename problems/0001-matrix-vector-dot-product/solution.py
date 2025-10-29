def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	mdv = []
	if len(b)!=len(a):
		return -1
	else: 
		for i in range(len(a)):
			temp = 0
			for j in range(len(a[0])):
				c = a[i][j] * b[j]
				av = temp + c
				temp = av
			mdv.append(temp)
	return mdv
