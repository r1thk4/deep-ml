import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	mat = np.array(matrix)
	eigenvalues = np.linalg.eig(mat)
	return eigenvalues[0]