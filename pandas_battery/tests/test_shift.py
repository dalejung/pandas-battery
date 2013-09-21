from pandas_battery.proving_ground import proving_ground
from pandas_battery.target.api import all_targets


class ShiftBattery(object):
    def test_shift(self):
        obj = self._construct()
        obj.shift(1)

    def test_shift_negative(self):
        obj = self._construct()
        obj.shift(-1)

proving_ground(all_targets, ShiftBattery)

if __name__ == '__main__':
    import nose                                                                      
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb', '--pdb-failure'],exit=False)   
