from collections import OrderedDict
import itertools

import pandas as pd
import numpy as np

import pandas.util.testing as tm
from pandas_battery.tools.attrdict import attrdict
from pandas_battery.target.frame import frame_targets

__all__ = ['panel_targets']


ITEMS_COUNT = 20

item_types = OrderedDict()
item_types['int'] = range(ITEMS_COUNT)
item_types['float'] = np.random.randn(ITEMS_COUNT)
item_types['bool'] = np.random.randn(ITEMS_COUNT) > 0
item_types['string'] = np.array([tm.rands(1) for x in range(ITEMS_COUNT)])
item_types['long_strings'] = np.array([tm.rands(30) for x in range(ITEMS_COUNT)])

target_args = itertools.product(frame_targets.items(), item_types.items())

def maker(frame_maker, items):
    def _maker():
        data = [frame_maker() for item in items]
        first = data[0]
        return pd.Panel(np.array([df.values for df in data]), items=items, 
                        minor_axis=first.columns, major_axis=first.index)
    return _maker

panel_targets = attrdict()
for args in target_args:
    frame_maker, items = args
    item_type, items = items # unpack (key, name)
    frame_name, frame_maker = frame_maker # unpack (key, name)
    obj_name = '_'.join([frame_name, item_type, 'panel'])
    panel_targets[obj_name] = maker(frame_maker, items)
