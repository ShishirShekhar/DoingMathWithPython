import pandas as pd
from sympy import FiniteSet
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

data = pd.read_csv("data.csv")
football = []
other = []

for i in range(data.shape[0]):
    if data.iloc[i, 1] == 1 :
        football.append(data.iloc[i, 0])
    if data.iloc[i, 2] == 1 :
        other.append(data.iloc[i, 0])

football = FiniteSet(*football)
other = FiniteSet(*other)


venn2(subsets=(football, other))
plt.show()