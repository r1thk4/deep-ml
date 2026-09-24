import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n = len(a)
	m = len(a[0])
	new_s = new_shape[0] * new_shape[1]
	if n * m != new_s:
		return []
	b = np.array(a)
	reshaped_matrix = b.reshape(new_shape)
	return reshaped_matrix