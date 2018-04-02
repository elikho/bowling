import unittest
from bowling import (
    GAME,
    get_frames, get_score,
)


class TestBowling(unittest.TestCase):

    def test_balls_instance(self):
        for ball in GAME:
            self.assertIsInstance(ball, int)

    def test_frames_count(self):
        self.assertEqual(len(get_frames(GAME)), 10)

    def test_balls_count(self):
        frames = get_frames(GAME)
        for i in frames:
            if i == 10: # last frame
                self.assertIn(len(frames[i]), [2, 3])
            else:
                self.assertIn(len(frames[i]), [1, 2])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBowling)
    unittest.TextTestRunner(verbosity=2).run(suite)
