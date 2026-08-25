import unittest

class MyTestCase(unittest.TestCase):

    def test_one(self):

        self.assertTrue(100 > 97,"sould be true")

    def test_two(self):

        self.assertEqual(10 + 20, 30, "should be 30")

    def test_tree(self):

        self.assertGreater(100, 80, "sould be True")

if __name__ == "__main__":

    unittest.main()