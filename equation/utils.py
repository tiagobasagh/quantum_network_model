import math


def linear_function(x, m, b):
	return m*x  + b


def poisson_coordenates(lamda, k):
	""" 
	:param int lamda: mean of degree distribution to a poisson distribution.
	:param int k:  ????
	
	:return float: Value of a possion distributio P(lamda, k).
	"""
	return math.exp(-lamda)*lamda**k/math.factorial(k)


def make_vec_poisson(lamda, size):
	"""
	:param int lamda:  mean of degree distribution to a poisson distribution.
	:param int size: size of the array distribution.

	:return list: returnt a list like as poission distribution.
	"""
	return [poisson_coordenates(lamda, k) for k in range(size)]


def emptylist(size):
	"""
	create a empty list
	
	:param int size: longitud of the list. 

	:return list: empty  list with len = `size` 
	"""
	empty_list = []
	for i in range(0, size):
		empty_list.append([])

	return empty_list
