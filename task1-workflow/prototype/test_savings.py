"""Checks the time-saving formula against a hand calculation. Run: py -m unittest test_savings -v"""
import unittest

from savings import calculate, load


class SavingsFormula(unittest.TestCase):

    def test_matches_hand_calculation(self):
        r = calculate(load("params.json"))
        # by hand: 30 x 12 = 360 requests
        # old = 3 x 30 + 20 = 110 min, new = 10 + 1 x 15 + 12 = 37 min
        # gross = 360 x 73 = 26,280; review = 360 x 0.10 x 10 = 360; support = 360 x 0.20 x 10 = 720; setup = 600
        self.assertEqual(r["requests"], 360)
        self.assertEqual(r["old_per_request"], 110)
        self.assertEqual(r["new_per_request"], 37)
        self.assertAlmostEqual(r["gross"], 26280)
        self.assertAlmostEqual(r["net"], 26280 - 360 - 720 - 600)

    def test_staff_can_lose_time(self):
        """With these values, staff save 8 min/request but pay all review/support/setup."""
        r = calculate(load("params.json"))
        self.assertAlmostEqual(r["staff_net"], 360 * 8 - 360 - 720 - 600)


if __name__ == "__main__":
    unittest.main(verbosity=2)
