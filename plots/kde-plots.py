# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import seaborn as sb
from pandas import read_table


def kde(vals, xmin, xmax, bw):
    """Returns the kernel density estimation"""
    x = np.linspace(xmin, xmax, 1000)
    density = np.zeros_like(x)
    for val in vals:
        p = norm(val, bw).pdf(x)
        density = density + p
    density = density / len(vals)
    return density, x


#   Import data
df = read_table("profiles.txt")

#   Set figure styles
sb.set_style("ticks")
colors = sb.color_palette()

#   Set up plot grid
fig = plt.figure(figsize=(10, 10))
ax = fig.subplots(1, 2)

#   Set x-axis labels
xlabels = ["Natural Log Difference\nWT-IVT\nProfile = ln(rx/bg)",
           "Percent Decrease\n(IVT-WT)/IVT\nProfile = rx-bg"]
for i, xlabel in enumerate(xlabels):
    ax[i].set_xlabel(xlabel)

#   Grab pertinent data
isvalid = ~np.isnan(df["logpval"].values)
percentdiff = df["percentdecrease"].values[isvalid]
logdiff = -df["logdiff"].values[isvalid]
nm = (df["Modification"].values == "Nm")[isvalid]
psi = (df["Modification"].values == "Psi")[isvalid]
other = ~np.logical_or(nm, psi)


sb.stripplot(logdiff[other], ax=ax[0], color=colors[0], jitter=0.1)
sb.stripplot(logdiff[psi], ax=ax[0], color=colors[1], jitter=0.1)
sb.stripplot(logdiff[nm], ax=ax[0], color=colors[3], jitter=0.1)

density, x = kde(logdiff[other], -2, 4, 0.5)
ax[0].plot(x, density, color=colors[0], ls="-")
density, x = kde(logdiff[psi], -2, 4, 0.5)
ax[0].plot(x, density, color=colors[1], ls="-")
density, x = kde(logdiff[nm], -2, 4, 0.5)
ax[0].plot(x, density, color=colors[3], ls="-")

sb.stripplot(percentdiff[other], ax=ax[1], color=colors[0], jitter=0.1)
sb.stripplot(percentdiff[psi], ax=ax[1], color=colors[1], jitter=0.1)
sb.stripplot(percentdiff[nm], ax=ax[1], color=colors[3], jitter=0.1)

density, x = kde(percentdiff[other], -2, 4, 0.5)
ax[1].plot(x, density, color=colors[0], ls="-")
density, x = kde(percentdiff[psi], -2, 4, 0.5)
ax[1].plot(x, density, color=colors[1], ls="-")
density, x = kde(percentdiff[nm], -2, 4, 0.5)
ax[1].plot(x, density, color=colors[3], ls="-")

ax[0].invert_yaxis()
ax[0].invert_xaxis()
ax[0].set_xlim(0, 3)

ax[1].invert_yaxis()
ax[1].set_xlim(0, 2)

ax[1].legend(loc="upper right")

plt.show()
