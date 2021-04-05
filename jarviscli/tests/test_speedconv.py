import unittest
from tests import PluginTest
from plugins.speedconv import speedconv

class SpeedconvTest(PluginTest):
    """
    Testing that the speedconv function works properly

    Since the function does a large number of conversions using coefficients,
    getting an perfectly equal value is unlikely so the test is considered
    successful if the result is within 1/1000 of the expected result
    """
    def setUp(self):
        self.test = self.load_plugin(speedconv)

    def within_margin(self, v1, v2):
        return abs(v1 - v2) < 0.001

    def test_ms_conversions(self):
        # m/s to km/h
        ms_to_kmh = self.test.convert_speed(100, "m/s", "km/h")
        self.assertTrue(self.within_margin(ms_to_kmh, 360))

        # m/s to ft/s
        ms_to_fts = self.test.convert_speed(100, "m/s", "ft/s")
        self.assertTrue(self.within_margin(ms_to_fts, 328.084))

        # m/s to mi/h
        ms_to_mih = self.test.convert_speed(100, "m/s", "mi/h")
        self.assertTrue(self.within_margin(ms_to_mih, 223.694))

        # m/s to kn
        ms_to_kn = self.test.convert_speed(100, "m/s", "kn")
        self.assertTrue(self.within_margin(ms_to_kn, 194.384))

    def test_kmh_conversions(self):
        # km/h to ft/s
        kmh_to_ms = self.test.convert_speed(100, "km/h", "m/s")
        self.assertTrue(self.within_margin(kmh_to_ms, 27.7778))

        # km/h to ft/s
        kmh_to_fts = self.test.convert_speed(100, "km/h", "ft/s")
        self.assertTrue(self.within_margin(kmh_to_fts, 91.1344))

        # km/h to mi/h
        kmh_to_mih = self.test.convert_speed(100, "km/h", "mi/h")
        self.assertTrue(self.within_margin(kmh_to_mih, 62.1371))

        # km/h to kn
        kmh_to_kn = self.test.convert_speed(100, "km/h", "kn")
        self.assertTrue(self.within_margin(kmh_to_kn, 53.9957))

    def test_fts_conversions(self):
        # ft/s to m/s
        fts_to_ms = self.test.convert_speed(100, "ft/s", "m/s")
        self.assertTrue(self.within_margin(fts_to_ms, 30.48))

        # ft/s to km/h
        fts_to_kmh = self.test.convert_speed(100, "ft/s", "km/h")
        self.assertTrue(self.within_margin(fts_to_kmh, 109.728))

        # ft/s to mi/h
        fts_to_mih = self.test.convert_speed(100, "ft/s", "mi/h")
        self.assertTrue(self.within_margin(fts_to_mih, 68.1818))

        # ft/s to kn
        fts_to_kn = self.test.convert_speed(100, "ft/s", "kn")
        self.assertTrue(self.within_margin(fts_to_kn, 59.2484))

    def test_mih_conversions(self):
        # mi/h to m/s
        mih_to_ms = self.test.convert_speed(100, "mi/h", "m/s")
        self.assertTrue(self.within_margin(mih_to_ms, 44.704))

        # mi/h to km/h
        mih_to_kmh = self.test.convert_speed(100, "mi/h", "km/h")
        self.assertTrue(self.within_margin(mih_to_kmh, 160.934))

        # mi/h to ft/s
        mih_to_fts = self.test.convert_speed(100, "mi/h", "ft/s")
        self.assertTrue(self.within_margin(mih_to_fts, 146.667))

        # mi/h to kn
        mih_to_kn = self.test.convert_speed(100, "mi/h", "kn")
        self.assertTrue(self.within_margin(mih_to_kn, 86.8976))

    def test_kn_conversions(self):
        # kn to m/s
        kn_to_ms = self.test.convert_speed(100, "kn", "m/s")
        self.assertTrue(self.within_margin(kn_to_ms, 51.4444))

        # kn to km/h
        kn_to_kmh = self.test.convert_speed(100, "kn", "km/h")
        self.assertTrue(self.within_margin(kn_to_kmh, 185.2))

        # kn to ft/s
        kn_to_fts = self.test.convert_speed(100, "kn", "ft/s")
        self.assertTrue(self.within_margin(kn_to_fts, 168.781))

        # kn to mi/h
        kn_to_mih = self.test.convert_speed(100, "kn", "mi/h")
        self.assertTrue(self.within_margin(kn_to_mih, 115.078))

if __name__ == '__main__':
    unittest.main()