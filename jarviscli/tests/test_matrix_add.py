import unittest
from tests import PluginTest
from plugins import matrix_add

class MatrixTest(PluginTest):

    def setUp(self):
        self.test = self.load_plugin(matrix_add.addition)
    
    
    def addTest(self):
        initial = [[3,2,1],[1,2,3], [2,3,1]]
        next_matrix = [[1,2,3], [3,2,1], [2,1,3]]
        row = 3
        col = 3
        summation = [[4,4,4], [4,4,4], [4,4,4]]
        tested = self.test.run(initial,next_matrix, row, col)
        self.assertEqual(tested, summation)

    def TEST(self):
        self.test.run()
        self.assertEqual(1,1)    
  

if __name__ == "__main__":
    unittest.main()
    


