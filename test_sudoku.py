import unittest

from sudoku import Sudoku
class TestSudoku(unittest.TestCase):
    
    def test_state_wrong_values_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        self.assertNotEqual (sudoku.no_delete, [(0, 3), (0, 1), (0, 4), (1, 0), (1, 3),
                                                (1, 4), (1, 5), (2, 1), (2, 2), (2, 7), 
                                                (3, 0), (3, 4), (3, 8), (4, 0), (4, 3), 
                                                (4, 5), (4, 8), (5, 0), (5, 4), (5, 8), (6, 1), 
                                                (6, 6), (6, 7), (7, 3), (7, 4), (7, 5), (7, 8), 
                                                (8, 4), (8, 7), (8, 8)])

    def test_state_wrong_values_4x4(self):
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        self.assertNotEqual (sudoku.no_delete, [(0, 3)])

    def test_state_values_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        self.assertEqual (sudoku.no_delete, [(0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), 
                                             (1, 5), (2, 1), (2, 2), (2, 7), (3, 0), (3, 4), 
                                             (3, 8), (4, 0), (4, 3), (4, 5), (4, 8), (5, 0), 
                                             (5, 4), (5, 8), (6, 1), (6, 6), (6, 7), (7, 3), 
                                             (7, 4), (7, 5), (7, 8), (8, 4), (8, 7), (8, 8)])

    def test_state_values_4x4(self):
        sudoku = Sudoku ([[4,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]])
        self.assertEqual (sudoku.no_delete, [(0, 0)])

    def test_not_change_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.not_change(0,3)
        self.assertTrue(total)

    def test_not_change_4x4(self):
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.not_change(0,3)
        self.assertTrue(total)

    def test_not_change_wrong_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.not_change(0,0)
        self.assertFalse(total)

    def test_not_change_wrong_4x4(self):
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.not_change(0,0)
        self.assertFalse(total)

    def test_no_row_repeat_wrong_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_row_repeat(3,3)
        self.assertFalse(total)

    def test_no_row_repeat_4x4(self):
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.no_row_repeat(2, 3)
        self.assertFalse(total)

    def test_no_row_repeat_9x9(self):
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_row_repeat(1,4)
        self.assertTrue(total)

    def test_no_row_repeat_good_4x4(self):
    
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.no_row_repeat(3, 3)
        self.assertTrue(total)

    def test_no_column_repeat_9x9(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_column_repeat(1,2)
        self.assertTrue(total)

    def test_no_column_repeat_4x4(self):
    
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.no_column_repeat(2, 2)
        self.assertTrue(total)

    def test_no_column_repeat_wrong_9x9(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_column_repeat(1,3)
        self.assertFalse(total)

    def test_no_repeat_zona_9x9(self):
            
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_repeat_zona(0,6,6)
        self.assertFalse(total)

    def test_no_repeat_zona_4x4(self):

        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.no_repeat_zona(1,1,4)
        self.assertFalse(total)

    def test_no_repeat_zona_good_9x9(self):
                       
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.no_repeat_zona(1,1,2)
        self.assertTrue(total)


    def test_no_repeat_zona_good_4x4(self):
            
        sudoku = Sudoku ([[4,3,0,0],
                          [2,0,0,1],
                          [0,2,3,0],
                          [1,0,0,0]])
        total = sudoku.no_repeat_zona(1,1,1)
        self.assertTrue(total)


    def test_insert_wrong_num(self):
    
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.insert_num(0,0,0)
        self.assertFalse(total)

    def test_insert_good_num(self):
        
        sudoku = Sudoku ([[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
        total = sudoku.insert_num(1,1,2)
        self.assertTrue(total)
        
    def test_win_9x9(self):
        
        sudoku = Sudoku ([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                          [6, 7, 2, 1, 9, 5, 3, 4, 8],
                          [1, 9, 8, 3, 4, 2, 5, 6, 7],
                          [8, 5, 9, 7, 6, 1, 4, 2, 3],
                          [4, 2, 6, 8, 5, 3, 7, 9, 1],
                          [7, 1, 3, 9, 2, 4, 8, 5, 6],
                          [9, 6, 1, 5, 3, 7, 2, 8, 4],
                          [2, 8, 7, 4, 1, 9, 6, 3, 5],
                          [3, 4, 5, 2, 8, 6, 1, 7, 9]])
        total = sudoku.win()
        self.assertTrue(total)

    def test_win_4x4(self):

        sudoku = Sudoku ([[4,3,1,2],
                          [2,1,3,4],
                          [3,2,4,1],
                          [1,4,2,3]])
        total = sudoku.win()
        self.assertTrue(total)

if __name__ == '__main__':

    unittest.main()