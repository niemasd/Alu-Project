#! /usr/bin/env python
'''
Niema Moshiri 2016

Generate histogram of sequnce lengths (excluding gaps) of intial PASTA MSA
'''
# imports
from matplotlib import rcParams
from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# settings
sns.set_style("ticks")
rcParams['font.family'] = 'serif'

# data (sequence lenths, excluding gaps, from initial PASTA MSA)

# create histogram
fig = plt.figure()
sns.distplot(data)
sns.plt.title("Initial PASTA MSA Sequence Lengths", fontsize=18, y=1.05)
sns.plt.xlabel("Sequence Length", fontsize=14)
sns.plt.ylabel("Frequency", fontsize=14)
sns.plt.show()
fig.savefig('original-PASTA-alignment-seq-lengths.png', bbox_inches='tight')
plt.close()