import unittest
from tests import PluginTest
from plugins.calories import Calories

class caloriesTest(PluginTest):
    """
        This class is testing the calories.py plugin
    """
    
    def setUp(self):
        self.test = self.load_plugin(Calories)

    def testCalories1(self):
        strings = {m, 35, 165, 70, 4}
        result = self.test.calories(jarvis, strings)
        self.assertEqual(result, 2720.73)
        
    def testCalories2(self):
        strings = {"m", 20, 184, 87, 4}
        result = self.test.calories(jarvis, strings)
        self.assertEqual(result, 3753.75)
        
    def testCalories3(self):
        strings = {"I", "Dont", "Know", "What", "Im", "doing"}
        result = self.test.calories(jarvis, strings)
        self.assertEqual(result, None)

    def testExercise_level1(self):
        level = 3
        result = self.test.exercise_level(level)
        self.assertEqual(result, 1.6)

    def testExercise_level2(self):
        level = 10
        result = self.test.exercise_level(level)
        self.assertEqual(result, 1)

