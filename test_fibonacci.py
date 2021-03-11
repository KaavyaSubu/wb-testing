import fibonacci
import unittest



class TestCase(unittest.TestCase):

    def fib(self):
        expectedList = [0,1,1,2,3,5,8,13,21,34]
        self.assertEqual(fibonacci.printFib(),expectedList)






if __name__ == '__main__':
    unittest.main()
