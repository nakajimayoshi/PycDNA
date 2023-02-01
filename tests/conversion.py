import unittest
from src.Cdna import Cdna

f = open("example_cds.txt", "r")
cds = f.read()

with open('example_converted_cds.txt') as y:
    manually_converted_cds = y.readlines()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        converted_cds = Cdna(cds).parse_to_cdna()
        self.assertEqual(converted_cds, ''.join(manually_converted_cds))


if __name__ == '__main__':
    unittest.main()
