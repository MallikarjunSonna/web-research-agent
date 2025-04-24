import unittest
from tools.search import google_search

class TestGoogleSearch(unittest.TestCase):
    def test_basic_query(self):
        results = google_search("What is AI?", num_results=2)
        self.assertTrue(len(results) > 0)
        self.assertIn("link", results[0])

if __name__ == "__main__":
    unittest.main()
