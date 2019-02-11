# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
from pandas import read_table

#   Import data
df = read_table("profiles.txt")

#   Define True positions
logpval = df["logpval"].values
isvalid = ~np.isnan(logpval)
logpval = logpval[isvalid]
pdiff = df["percentdecrease"].values[isvalid]
logdiff = df["logdiff"].values[isvalid]
nm = (df["Modification"].values == "Nm")[isvalid]
psi = (df["Modification"].values == "Psi")[isvalid]
other = (np.logical_not(np.logical_or(nm, psi)))

#   Set up plot grid
fig = plt.figure(figsize=(10, 10))
ax = fig.subplots(1, 1)

#   Color palette
sb.set_style("ticks")
colors = sb.color_palette()

#   Make scatter plot
ax.scatter(pdiff[other], logdiff[other], color=colors[0], label="all")
ax.scatter(pdiff[psi], logdiff[psi], color=colors[1], label="pseudouridines")
ax.scatter(pdiff[nm], logdiff[nm], color=colors[2], label="2'-O-Methyl")

ax.set_title("ln(wt/ivt) vs (ivt-wt)/ivt")
ax.legend(loc='lower left')
ax.set_xlabel('Percent Decrease\n(ivt-wt)/ivt')
ax.set_ylabel('Natural Log Difference')

plt.show()
