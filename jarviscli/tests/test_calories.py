import unittest
from tests import PluginTest
from plugins.calories import Calories
from Jarvis import Jarvis

class caloriesTest(PluginTest):
    """
        This class is testing the calories.py plugin
    """

    def setUp(self):
        self.test = self.load_plugin(Calories)

    def testCalories1(self):
        strings = {}
        strings[0] = "f"
        strings[1] = 35
        strings[2] = 165
        strings[3] = 70
        strings[4] = 4
        result = self.test.calories(Jarvis, strings)
        self.assertEqual(result, 2720.73)
        
    def testCalories2(self):
        strings = {}
        strings[0] = "m"
        strings[1] = 20
        strings[2] = 184
        strings[3] = 87
        strings[4] = 4
        result = self.test.calories(Jarvis, strings)
        self.assertEqual(result, 3753.75)
        
    def testCalories3(self):
        strings = {}
        strings[0] = "I"
        strings[1] = 20
        strings[2] = 20
        strings[3] = 30
        strings[4] = 20
        result = self.test.calories(Jarvis, strings)
        self.assertEqual(result, None)

    def testExercise_level1(self):
        level = 3
        result = self.test.exercise_level(level)
        self.assertEqual(result, 1.6)

    def testExercise_level2(self):
        level = 10
        result = self.test.exercise_level(level)
        self.assertEqual(result, 1)

