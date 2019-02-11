# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from sklearn import metrics
import seaborn as sb
from pandas import read_table

#   Import data
df = read_table("profiles.txt")

#   Define True positions
logpval = df["logpval"].values
isvalid = ~np.isnan(logpval)
logpval = logpval[isvalid]
score = df["percentdecrease"].values[isvalid]

nm = (df["Modification"].values == "Nm")[isvalid]
psi = (df["Modification"].values == "Psi")[isvalid]
both = np.logical_or(nm, psi)

#   Set up plot grid
fig = plt.figure(figsize=(18, 6))
axes = fig.subplots(1, 3)

#   Color palette
sb.set_style("ticks")
colors = sb.color_palette()

#   plot ROC for several p-value cutoffs
for x in xrange(0, 9, 2):
    threshold = logpval > x

    fpr, tpr, thresholds = metrics.roc_curve(nm[threshold], score[threshold])
    auc = metrics.auc(fpr, tpr)
    axes[0].plot(fpr, tpr, color=colors[x - 4],
                 label='P < 10^-{0} , AUC = {1:10.3f}'.format(x, auc))

    fpr, tpr, thresholds = metrics.roc_curve(both[threshold], score[threshold])
    auc = metrics.auc(fpr, tpr)
    axes[1].plot(fpr, tpr, color=colors[x - 4],
                 label='P < 10^-{0} , AUC = {1:10.3f}'.format(x, auc))

axes[0].set_title("Receiver Operating Characteristic\nNm sites only")
axes[0].plot([0, 1], [0, 1], 'r--')
axes[0].set_ylabel('True Positive Rate')
axes[0].set_xlabel('False Positive Rate')
axes[0].set_ylim([0, 1])
axes[0].set_xlim([0, 1])
axes[0].legend(loc='lower right')

axes[1].set_title("Receiver Operating Characteristic\nNm and Psi sites")
axes[1].plot([0, 1], [0, 1], 'r--')
axes[1].legend(loc='lower right')
axes[1].set_xlim([0, 1])
axes[1].set_ylim([0, 1])
axes[1].set_xlabel('False Positive Rate')

axes[2].set_title('p-value vs Percent Decrease "Volcano Plot"')
axes[2].scatter(score[~both], logpval[~both], color=colors[0])
axes[2].scatter(score[psi], logpval[psi], color=colors[1])
axes[2].scatter(score[nm], logpval[nm], color=colors[3])
axes[2].set_xlim(0, 1.5)
axes[2].set_ylabel('-log10(p-value)')
axes[2].set_xlabel('Percent Decrease\n(IVT-WT)/IVT')

plt.show()
