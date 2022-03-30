import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # add assertion here

    def test_something2(self):
        test_param = 'asdasd'
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))  # add assertion here
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
