from pandas_battery.proving_ground import proving_ground
from pandas_battery.target.api import all_targets

def _single_dtype(obj):
    if hasattr(obj, 'dtype'):
        return obj.dtype
    if hasattr(obj, 'dtypes'):
        dtypes = obj.dtypes.unique()
        if len(dtypes) == 1:
            return dtypes[0]
    return None

class ArithOpsBattery(object):
    def test_mul(self):
        obj = self._construct()
        dtype = _single_dtype(obj)
        test_result = None
        test = obj.iloc[0]
        try:
            test_result = test * test
        except Exception as e:
            test_result = e

        try:
            result = obj * obj
        except Exception as e:
            result = e

        if isinstance(result, Exception): 
            if isinstance(result, type(test_result)):
                pass
            else:
                raise result


proving_ground(all_targets, ArithOpsBattery)

if __name__ == '__main__':
    import nose                                                                      
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],exit=False)   
