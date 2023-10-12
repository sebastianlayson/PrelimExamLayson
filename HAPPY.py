import unittest


class happyEqual(unittest.TestCase):
    def testEqual(self):
        word = "Sad"
        happy = "Happy"
        self.assertEqual (word,happy)    

if __name__ == "__main__":
    unittest.main()