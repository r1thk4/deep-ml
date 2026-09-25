import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	a = np.array(A)
	t = np.array(T)
	if np.linalg.det(t) == 0:
		return -1	
	s = np.array(S)
	if np.linalg.det(s) == 0:
		return -1
	t_in = np.linalg.inv(t)
	intermediate = np.matmul(t_in, a)
	transformed_matrix = np.matmul(intermediate, s)
	return transformed_matrix