import matplotlib.pyplot as plt 
import numpy as np

import entropy_analysis as ea
from fit_analysis import fix_size, fix_lamda
from tools import make_list_files
from plots import same_curve_plots_fix_N, same_curve_plots_fix_L





plt.figure(1)

#same_curve_plots_fix_L('cm_poisson_{}_{}', 'N={}', 10, 1000, 19000)
"""
s = []
labels=[]
"""
s = []
labels=[]
entropy, max_entropy = ea.calculate_entropy('05_pt_er_20000')
s.append(entropy)
label = 'ER'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=111)
"""

entropy, max_entropy = ea.calculate_entropy('bar_3_10000')
s.append(entropy)
label = 'BA(3, 10000)'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=312)

entropy, max_entropy = ea.calculate_entropy('bar_5_10000')
s.append(entropy)
label = 'BA(5, 10000)'
labels.append(label)
ea.plot_entropy([entropy], [label],max_entropy, pos=313)

plt.suptitle(f'Barabasi-Albert')
"""

plt.show()
