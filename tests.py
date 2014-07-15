import unittest
import bejeweled

class Tests(unittest.TestCase):

    def setUp(self):
        self.game = bejeweled.Game("test-board")

    def test_init(self):
        self.assertEqual(str(self.game),
                         "00011\n"
                         "02221\n"
                         "10222")

    def test_jewel_at(self):
        self.assertEqual(self.game.jewel_at(0,0), 0)
        self.assertEqual(self.game.jewel_at(0,3), 1)
        self.assertEqual(self.game.jewel_at(2,0), 1)

    def test_group(self):
        self.assertSetEqual({(0, 0), (0, 1), (0, 2), (1, 0)},
                            set(self.game.group(0, 0)))
        self.assertSetEqual({(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (2, 4)},
                            set(self.game.group(1, 1)))

    def test_remove(self):
        game = bejeweled.Game("test-board")
        game.remove(0,0)
        self.assertEqual(str(game),
                         "   11\n"
                         " 2221\n"
                         "10222")

        game = bejeweled.Game("test-board")
        game.remove(1,1)
        self.assertEqual(str(game),
                         "00011\n"
                         "0   1\n"
                         "10   ")

    def test_gravity(self):
        game = bejeweled.Game("test-board")
        game.remove(1, 1)
        game.shake()
        self.assertEqual(str(game),
                         "0    \n"
                         "00  1\n"
                         "10011")

if __name__ == "__main__":
    unittest.main()
