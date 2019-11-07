import unittest
from interfaz import Interfaz

class Test_Interfaz(unittest.TestCase):

    def setUp(self):
        self.num = Interfaz()
    
    def test_enter_number(self):
        if Interfaz.enter_number(0,-2,2,10):
            return self.assertTrue
    
    def test_ask_value(self):
        if self.num:
            return self.assertTrue

    def test_play(self):
        if Interfaz.play:
            return self.assertTrue    
 
if __name__ == '__main__':
    unittest.main()