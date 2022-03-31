import unittest
import randomgame


class MyTestCase(unittest.TestCase):
    def test_something(self):
        choice = 2
        r = 2
        result = randomgame.run_guess(choice, r)
        self.assertTrue(result)

    def test_something1(self):
        choice = 1
        r = 2
        result = randomgame.run_guess(choice, r)
        self.assertFalse(result)

    def test_something2(self):
        choice = 4
        r = 2
        result = randomgame.run_guess(choice, r)
        self.assertFalse(result)

    def test_something3(self):
        r = 2
        result = randomgame.run_guess('2', r)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
