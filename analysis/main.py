import entropy_analysis as ea
s = []
labels = []
entropy, max_entropy = ea.calculate_entropy('erdos_renyi_10000')
s.append(entropy)
labels.append('wachin')
ea.plot_entropy(s, labels, max_entropy)