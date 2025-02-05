import unittest
from tests import PluginTest
from plugins.matrix_add import Matrix
from Jarvis import Jarvis

class Matrix_addTest(PluginTest):

    def setUp(self):
        self.test = self.load_plugin(Matrix)

    def testSum(self): 
        m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        row = 3
        col = 3
        result = self.test.sum(m1, m2, row, col)
        check = [[10, 10, 10],[10, 10, 10],[10, 10, 10]]
        self.assertEqual(result, check)

    def testNotSquare(self): 
        m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [10, 11, 12]]
        row = 3
        col = 4
        result = self.test.sum(m1, m2, row, col)
        check = [[10, 10, 10],[10, 10, 10],[10, 10, 10], [22,22,22]]
        self.assertEqual(result, check)  
    

