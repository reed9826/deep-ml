import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	det = (matrix[0][0]*matrix[1][1]) -( matrix[0][1]*matrix[1][0])
	trace = matrix[0][0] + matrix[1][1]
	
	b = trace
	c = det

	def root(a,b,c):
        d = b**2 - 4*a*c 
		r1 =( -b + math.sqrt(d))/ (2*a)
		r2 = (-b - math.sqrt(d) )/ (2*a)

		return [r1, r2]
	eigenvalues = root(1, -b, c)
	return eigenvalues