from collections import OrderedDict
import itertools

import pandas as pd
import numpy as np

import pandas.util.testing as tm
from pandas_battery.tools.attrdict import attrdict

__all__ = ['frame_targets']

N = 10000
COLS = 5
FLAT_N = N * COLS
shape = (N, COLS)

data_types = OrderedDict()
data_types['int'] = range(N)
data_types['float'] = np.random.randn(N)
data_types['bool'] = np.random.randn(N) > 0
data_types['string'] = np.array([tm.rands(1) for x in range(FLAT_N)]).reshape(shape)
data_types['long_strings'] = np.array([tm.rands(30) for x in range(FLAT_N)]).reshape(shape)

indexes = OrderedDict()
indexes[''] = None
indexes['time'] = pd.date_range(start="2000", freq="D", periods=N)
indexes['period'] = pd.period_range(start="2000", freq="D", periods=N)

column_types = OrderedDict()
column_types[''] = None
column_types['strcol'] = [tm.rands(10) for x in range(COLS)]

target_args = itertools.product(data_types, indexes, column_types)

def maker(data, index, columns):
    def _maker():
        arr = np.array(data)
        # repeat the data for each column
        if arr.ndim == 1:
            arr = np.repeat(arr.ravel(), COLS).reshape(shape)
        return pd.DataFrame(arr, index=index, columns=columns)
    return _maker

frame_targets = attrdict()
for args in target_args:
    data_type, index_type, column_type = args
    obj_name = '_'.join(bit for bit in list(args) + ['frame'] if bit)
    data = data_types[data_type]
    index = indexes[index_type]
    columns = column_types[column_type]
    frame_targets[obj_name] = maker(data, index, columns)
