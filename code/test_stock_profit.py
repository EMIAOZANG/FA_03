import unittest
from stock_profit import *
from stock_profit_linear import *

class TestMaxMinMaxSubarray(unittest.TestCase):
    def setUp(self):
        self.input_cases = [[1,2,3,4,5],
                [9,8,7,6,5,4],
                [1,2,3,4,4,3,2,1],
                [4,4,4,4,4,4,4,4],
                [1,2,1,2,1,2,1],
                [9,8,7,6,5,6,7,8],
                [2,2,2,3,3,3,3,4,4],
                [1,2,3,4,5,4,3,2,3,4,5,6,5,4,3,4],
                [9,8,7,6,5,6,7,8,7,6,5,4,5,6,7,6,5,4,3]]
        self.outputs = [(0,4,0,4,4),
                (5,0,0,0,0)]

#    def TestStockProfit(self):
#        for input_case in self.input_cases:
#            print input_case
#            print max_min_maxsubarray(input_case,0,len(input_case)-1)

    def runTest(self):
        for input_case in self.input_cases:
            print input_case
            print max_profit(input_case)
        

if __name__ == "__main__":
    unittest.main()



