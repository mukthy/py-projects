import unittest
import main


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("Testing is starting")

    def test_something(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # add assertion here

    def test_something2(self):
        test_param = 'asdasd'
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))  # add assertion here
        self.assertIsInstance(result, ValueError)

    def test_something3(self):
        test_param = None
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))  # add assertion here
        self.assertEqual(result, 'Please enter a number')

    def test_something4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))  # add assertion here
        self.assertEqual(result, 'Please enter a number')

    def test_something5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))  # add assertion here
        self.assertEqual(result, 'Please enter a number')


if __name__ == '__main__':
    unittest.main()
