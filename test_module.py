import unittest
from demographic_data_analyzer import calculate_demographic_data

class DemographicAnalyzerTest(unittest.TestCase):

    def test_function_runs(self):
        result = calculate_demographic_data(False)
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()
