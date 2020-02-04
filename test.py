import unittest
from main import _countdown


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

    # def test_countdown_start(self):
    #     r = _countdown(blockheight=614000)
    #     self.assertEqual("", r)



if __name__ == '__main__':
    unittest.main()
