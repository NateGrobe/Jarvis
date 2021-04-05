import unittest
from tests import PluginTest
from plugins.tic_tac_toe import TicTacToe
from Jarvis import Jarvis

board = {'7': '   ', '8': '   ', '9': '   ',
         '4': '   ', '5': '   ', '6': '   ',
         '1': '   ', '2': '   ', '3': '   '}

class TictactoeTest(PluginTest):
    
    def setUp(self):
        self.test = self.load_plugin(TicTacToe)

    def testcheckWinner1(self):
        board = {'7': '   ', '8': ' X ', '9': ' O ',
         '4': '   ', '5': ' O ', '6': ' X ',
         '1': ' O ', '2': '   ', '3': ' X '}
        result = self.test.checkWinner(board, Jarvis, ' O ')
        self.assertTrue(result)

    def testcheckWinner2(self):
        board = {'7': '   ', '8': ' X ', '9': '   ',
         '4': ' O ', '5': ' O ', '6': ' O ',
         '1': ' X ', '2': ' X ', '3': '   '}
        result = self.test.checkWinner(board, Jarvis, ' O ')
        self.assertTrue(result)

    def testcheckWinner3(self):
        board = {'7': ' X ', '8': ' O ', '9': ' X ',
         '4': '   ', '5': ' X ', '6': ' O ',
         '1': ' X ', '2': ' O ', '3': '   '}
        result = self.test.checkWinner(board, Jarvis, ' X ')
        self.assertTrue(result)

    def testcheckWinner4(self):
        board = {'7': ' X ', '8': ' X ', '9': ' X ',
         '4': '   ', '5': '   ', '6': ' O ',
         '1': '   ', '2': ' O ', '3': ' O '}
        result = self.test.checkWinner(board, Jarvis, ' O ')
        self.assertTrue(result)
    
    def testcheckWinner5(self):
        board = {'7': ' X ', '8': '   ', '9': ' O ',
         '4': ' X ', '5': ' O  ', '6': '   ',
         '1': ' X ', '2': ' O ', '3': '   '}
        result = self.test.checkWinner(board, Jarvis, ' X ')
        self.assertTrue(result)

    def testcheckWinner6(self):
        board = {'7': ' X ', '8': ' O ', '9': '   ',
         '4': ' X ', '5': ' O ', '6': '   ',
         '1': '   ', '2': ' O ', '3': ' X '}
        result = self.test.checkWinner(board, Jarvis, ' O ')
        self.assertTrue(result)

    def testcheckWinner7(self):
        board = {'7': '  X ', '8': ' O ', '9': ' X ',
         '4': ' O ', '5': ' X  ', '6': ' O ',
         '1': ' O ', '2': ' X ', '3': ' O  '}
        result = self.test.checkWinner(board, Jarvis, ' O ')
        self.assertFalse(result)