# -- encoding:utf-8 --

import matplotlib.pyplot as pyplot
import numpy
import pandas

time_money = pandas.read_csv('money_supply.csv')

t = time_money.T.values[0]
m = time_money.T.values[1]
x = numpy.arange(1, len(t) + 1)

pyplot.plot(x, m)

pyplot.xlabel('Time(s)')
pyplot.xticks(x, t.tolist(), rotation=45)

pyplot.ylabel('M2')

pyplot.title('Money Supply Unit:100 Million Yuan')

pyplot.grid(True)

pyplot.savefig("Money_Supply.png")
pyplot.show()
