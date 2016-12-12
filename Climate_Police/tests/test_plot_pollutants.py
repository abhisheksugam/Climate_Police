#run the test with default values of df, state and year 


import unittest
from plot_pollutants import plot_pollutants
import pandas as pd


df = pd.read_csv("../data/pollution_us_2000_2016.csv")
year="2010"
state="Arizona"

class TestPlot(unittest.TestCase):
  
    def testPlotPollutants(self):
        
        result=plot_pollutants(df, year, state)
        expected_explanation="Levels of pollutants plotted."
        self.assertTrue(result, expected_explanation)

if __name__ == '__main__':
    unittest.main()