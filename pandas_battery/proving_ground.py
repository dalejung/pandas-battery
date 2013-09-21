import unittest
import inspect

def proving_ground(targets, battery):
    """
        ind = pd.date_range(start="2000", freq="D", periods=10)
        targets = {}
        targets['int_series'] = lambda : pd.Series(range(10))
        targets['bool_series'] = lambda : pd.Series(np.random.randn(10) > 0, index=ind)
        targets['float_series'] = lambda : pd.Series(np.random.randn(10))
        targets['string_series'] = lambda : pd.Series(list('asdfqwerzx'), index=ind)

        class ShiftBattery(object):
            def test_check(self):
                obj = self._construct()
                if obj.is_time_series:
                    assert False, "Don't support time series"

        setup_battery(targets, ShiftBattery)
    """
    # global module scope of the calling function
    caller_globals = inspect.stack()[1][0].f_globals
    battery_name = battery.__name__
    # create a unittest.TestCase subclass for each target
    for target, maker in targets.items():
        cls_name = "Test" + battery_name + '_' + target
        cls = makeClass(cls_name, battery, maker)
        caller_globals[cls_name] = cls

def makeClass(cls_name, battery, maker):
    cls = type(cls_name, (unittest.TestCase, battery), {})
    cls._construct = lambda self: maker()
    return cls
