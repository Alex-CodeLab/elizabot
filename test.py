import unittest
from commands.countdown import _countdown
from commands.halving import _halving

class TestMethods(unittest.TestCase):

    def test_true(self):
        #test test
        self.assertEqual(True, True)

    def test_countdown(self):
        r = _countdown(blockheight=615916)
        self.assertEqual("Next fast in 84 blocks (13.5 hours).", r)

    def test_countdown_false(self):
        r = _countdown(blockheight=611000)
        self.assertNotEqual("Next fast in 84 blocks (13.5 hours).", r)

    def test_countdown_almost(self):
        r = _countdown(blockheight=611999)
        self.assertEqual("Next fast in 1 blocks (0.2 hours).", r)

    def test_haliving(self):
        r = _halving()
        self.assertEqual("Blocks until halving:", r[:21])




if __name__ == '__main__':
    unittest.main()
