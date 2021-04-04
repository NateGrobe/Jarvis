import unittest
from tests import PluginTest
from plugins.speedtest import pretty_speed

class testSpeedtest:

    def setUp(self):
        self.test = self.load_plugin(Calories)

    def test_pretty_speed1(self):
        speed = 153490212075
        result = self.test.pretty_speed(speed)
        self.assertEqual(result, "153.49 Gbps")

    def test_pretty_speed2(self):
        speed = 12349
        result = self.test.pretty_speed(speed)
        self.assertEqual(result, "12.49 Kbps")
    
    def test_pretty_speed3(self):
        speed = 14
        result = self.test.pretty_speed(speed)
        self.assertEqual(result, "14 bps")

    def test_pretty_speed4(self)
        speed = 123490075
        result = self.test.pretty_speed(speed)
        self.assertEqual(result, "123.49 Mbps")