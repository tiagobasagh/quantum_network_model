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


def list_to_dict(key_list):
	key_dict = {}
	for k in range(max(key_list)+1):
		key_dict[k]= 0

	return key_dict

def clean_dict(dic, init):
	aux_dic = dic
	for k in dic.keys():
		aux_dic[k] = init

	return aux_dic