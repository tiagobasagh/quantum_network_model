import math

import matplotlib.pyplot as plt


def N_s(mu, s):
	return (mu**s - 1)/(mu -1)


def C_k(mu, k):
	return mu**k


def big_component(mu, s):
		return 1 + (mu - 2) * N_s(mu, s)


def entropy(p):
	return -p * math.log(p)


def entropy_big_component(mu, s):
	N = N_s(mu, s)
	N_short = big_component(mu, s-1)
	p = N_short/N
	
	return entropy(p)


def entropy_small_components(mu, s):
	e_small_componets = 0
	N = N_s(mu, s)
	for k in range(s-1):
		e_small_componets += 2*entropy(C_k(mu, k)/N)
	
	return e_small_componets
	

def fix_mu(mu, initial_s, large_limit):
	x = range(initial_s, large_limit)
	y = []
	for s in x:
		eb = entropy_big_component(mu, s)
		es = entropy_small_components(mu, s)
		y.append(eb + es)
	return x, y


def fix_generaciones(s, mu_min, mu_max):
	x = range(mu_min, mu_max+1)
	y = []
	for mu in x:
		eb = entropy_big_component(mu, s)
		es = entropy_small_components(mu, s)
		y.append(eb + es)
	return x, y


def max_entropy(mu, s):
	N = int(N_s(mu, s))

	return math.log(N)


plt.figure(1)
for u in range(2, 7):
	x, y = fix_mu(u, 3, 13)
	plt.hlines(max(y), min(x), max(x), linestyles='dashed')
	plt.plot(x, y, label=f'mu:{u} - Entropia: {int(100*max(y))/100}')

plt.title('Removiendo el camino en un Árbol de Galton-Watson')
plt.xlabel('Generaciones')
plt.ylabel('Entropía')
plt.legend()
plt.show()
