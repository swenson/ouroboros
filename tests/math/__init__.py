import binascii
from ouroboros.math.floatint import float2int
import random
import struct
import unittest

class TestFloat2Int(unittest.TestCase):

    def setUp(self):
        random.seed(1234)

    def test_random_values(self):
        for i in range(1000):
            r = random.random()
            self.assertEqual(
                hex(int(binascii.hexlify(struct.pack('>d', r)), 16)),
                hex(float2int(r)))

if __name__ == '__main__':
    unittest.main()
