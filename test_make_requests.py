import unittest
import make_requests


class TestRequest(unittest.TestCase):

    def test_url(self):
        result = make_requests.test_url()
        self.assertRaisesRegex(ValueError, r'[a-zA-Z0-9.-]+\.(com|edu|net|gov)')



if __name__ == '__main__':
    unittest.main()

