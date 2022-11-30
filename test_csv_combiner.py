import unittest
from pandas.testing import assert_frame_equal
import pandas as pd

class TestMain(unittest.TestCase):
    def one_fixture_test(self): #test for one argument
        combined = pd.read_csv("combined.csv")
        filename = "accessories.csv"
        accessories_df = pd.read_csv("./fixtures/accessories.csv")
        accessories_df.insert(loc=2, column="filename", value=filename)
        assert_frame_equal(accessories_df, combined)
    
    def two_fixture_test(self): #test for two arguments
        combined = pd.read_csv("combined.csv")
        filename = "accessories.csv"
        accessories_df = pd.read_csv("./fixtures/accessories.csv")
        accessories_df.insert(loc=2, column="filename", value=filename)
        filename2 = "clothing.csv"
        clothing_df = pd.read_csv("./fixtures/clothing.csv")
        clothing_df.insert(loc=2, column="filename", value=filename2)
        test_df = pd.concat([accessories_df, clothing_df])
        assert_frame_equal(test_df, combined)
    
    def three_fixture_test(self): #test for three arguments
        combined = pd.read_csv("combined.csv")
        filename = "accessories.csv"
        accessories_df = pd.read_csv("./fixtures/accessories.csv")
        accessories_df.insert(loc=2, column="filename", value=filename)
        filename2 = "clothing.csv"
        clothing_df = pd.read_csv("./fixtures/clothing.csv")
        clothing_df.insert(loc=2, column="filename", value=filename2)
        filename3 = "household_cleaners.csv"
        hhc_df = pd.read_csv("./fixtures/household_cleaners.csv")
        hhc_df.insert(loc=2, column="filename", value=filename3)
        test_df = pd.concat([accessories_df, clothing_df, hhc_df])
        assert_frame_equal(test_df, combined)


if __name__ == '__main__':
    unittest.main()