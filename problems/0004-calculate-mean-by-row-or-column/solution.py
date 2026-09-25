import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	x = 1
	if mode == "column":
		x = 0
	means = np.mean(matrix, axis=x)
	return means