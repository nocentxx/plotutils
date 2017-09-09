# -- encoding:utf-8 --

import matplotlib.pyplot as pyplot
import numpy
import pandas

x_label = 'Time(s)'
y_label = 'M2'
plot_title = 'Money Supply Unit:100 Million Yuan'
ms_png_name = 'money_supply.png'

time_money = pandas.read_csv('money_supply.csv')

t = time_money.T.values[0]
m = time_money.T.values[1]
x = numpy.arange(1, len(t) + 1)

pyplot.plot(x, m, 'ro-')

pyplot.xlabel(x_label)
pyplot.xticks(x, t.tolist(), rotation=45)

pyplot.ylabel(y_label)

pyplot.title(plot_title)

pyplot.grid(True)

pyplot.savefig(ms_png_name)
pyplot.show()
