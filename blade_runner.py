#
import numpy
import pandas
import seaborn
from matplotlib import pyplot

#


#
weights = pandas.read_excel('C:/Users/Edward/Desktop/weights.xlsx').set_index('date')
prices = pandas.read_excel('C:/Users/Edward/Desktop/prices.xlsx').set_index('date')

# capital = 1_000_000  # $
# capital = 440  # $

from aster.asterfunc import evaluate


capitals = [100, 200, 300, 400, 500, 5000, 2000, 5000, 10000, 100000, 1000000]
ylds = []
relative = [x / prices.values[0, :].max() for x in capitals]
re_vie = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
for capital in capitals:

    tl_capital, tl_c1, tl_c2, tl_r, kk = evaluate(y=prices.values, w=weights.values, capital_value=capital)
    ylds.append(tl_capital[-1] / capital)
"""

for vie in re_vie:
    tl_capital, tl_c1, tl_c2, tl_r, kk = evaluate(y=prices.values[vie:], w=weights.values[vie:], capital_value=capitals[5])
    # ylds.append((tl_capital[-1] / capitals[5]) ** (12/weights.values[vie:].shape[0]))
    ylds.append(tl_capital[-1] / capitals[5])

yldsa = []

for vie in re_vie:
    tl_capital, tl_c1, tl_c2, tl_r, kk = evaluate(y=prices.values[vie:], w=weights.values[vie:], capital_value=capitals[-1])
    # ylds.append((tl_capital[-1] / capitals[5]) ** (12/weights.values[vie:].shape[0]))
    yldsa.append(tl_capital[-1] / capitals[-1])

hugo = pandas.DataFrame(data={'start': re_vie, 'perf': ylds, 'perf_ideal': yldsa, 'w': weights.values[:11, 0]})

"""
fig, ax = pyplot.subplots(2, 1)
ax[0].plot(prices.index, numpy.array(tl_capital), 'black')
ax[1].plot(prices.index[1:], numpy.array(tl_c1), 'orange',
           prices.index[1:], numpy.array(tl_c2), 'navy',
           prices.index[1:], numpy.array(tl_r), 'gray')
"""

"""
stacked = pandas.DataFrame(data={'ts': prices.index[1:], 'IVV': tl_c1, 'TLT': tl_c2, 'Cash': tl_r})
stacked = stacked.set_index('ts')
stacked.plot(kind='bar', stacked=True)
"""
