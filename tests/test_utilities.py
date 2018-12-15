import unittest
from src import utilities


class UtilitiesTest(unittest.TestCase):
    def test_dec_to_reversed_bin(self):
        self.assertEqual(utilities.dec_to_bin(63), "111111")
        self.assertEqual(utilities.dec_to_bin(64), "0000001")
        self.assertEqual(utilities.dec_to_bin(350), "011110101")

    def test_reversed_bin_to_dec(self):
        self.assertEqual(utilities.bin_to_dec("1000101"), 81)
        self.assertEqual(utilities.bin_to_dec("100000000000"), 1)
        self.assertEqual(utilities.bin_to_dec("100000000001"), 2049)

    def test_correct_length(self):
        self.assertEqual(utilities.make_length_correct(21), 21)
        self.assertEqual(utilities.make_length_correct(1910), 1014)
        self.assertEqual(utilities.make_length_correct(341), 213)
