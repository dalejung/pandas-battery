from collections import OrderedDict
import itertools

import pandas as pd
import numpy as np

__all__ = ['series_targets']

N = 10

indexes = OrderedDict()
indexes[''] = None
indexes['time'] = pd.date_range(start="2000", freq="D", periods=N)
indexes['period'] = pd.period_range(start="2000", freq="D", periods=N)


data_types = OrderedDict()
data_types['int'] = range(10)
data_types['float'] = np.random.randn(N)
data_types['bool'] = np.random.randn(N) > 0
data_types['string'] = list('asdfqwerzx')

target_args = itertools.product(data_types, indexes)

def maker(data, index):
    def _maker():
        return pd.Series(data, index=index)
    return _maker

series_targets = OrderedDict()
for data_type, index_type in target_args:
    series_name = '_'.join(bit for bit in [data_type, index_type, 'series'] if bit)
    data = data_types[data_type]
    index = indexes[index_type]
    series_targets[series_name] = maker(data, index)
