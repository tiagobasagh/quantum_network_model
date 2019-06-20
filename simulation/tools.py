import numpy as np

def make_distribution(size, scale, name, loc):
	dic_distributions = {'poisson': np.random.poisson,
	                     'power': np.random.power,
	                     'normal': np.random.normal,
	                     'exponential': np.random.exponential}

	if loc:
		distribution = dic_distributions[name](loc, scale, size)
	else:
		distribution = dic_distributions[name](scale, size)

	return distribution.tolist()