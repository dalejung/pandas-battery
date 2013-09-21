from pandas_battery.target.series import series_targets
from pandas_battery.target.frame import frame_targets
from pandas_battery.tools.attrdict import attrdict

def merge_dict(*dicts):
    results = attrdict()
    for dict in dicts:
        for k, v in dict.items():
            if k in results:
                raise Exception("Key already exists")
            results[k] = v
    return results

all_targets = merge_dict(series_targets, frame_targets)
