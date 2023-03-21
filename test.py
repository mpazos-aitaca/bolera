import unittest

from Exceptions import *
from Game import Game


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Game()

    def lanzar_varios(self, n, bolos):
        for _ in range(n):
            self.g.lanzar(bolos)

    def lanzar_semipleno(self):
        self.g.lanzar(5)
        self.g.lanzar(5)

    def lanzar_pleno(self):
        self.g.lanzar(10)

    def test_gutter_game(self):
        self.lanzar_varios(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.lanzar_varios(20, 1)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        self.lanzar_spare()
        self.g.lanzar(3)
        self.lanzar_varios(17, 0)
        self.assertEqual(self.g.score(), 16)

    def test_one_strike(self):
        self.lanzar_pleno()
        self.g.lanzar(3)
        self.g.lanzar(4)
        self.lanzar_varios(16, 0)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        self.lanzar_varios(12, 10)
        self.assertEqual(self.g.score(), 300)

    def test_roll_of_greater_than_10_raises_error(self):
        with self.assertRaises(RollError):
            self.g.lanzar(11)

    def test_negative_roll_raises_error(self):
        with self.assertRaises(RollError):
            self.g.lanzar(-1)

    def test_frame_rolls_in_sum_greater_than_10_raises_error(self):
        self.lanzar_pleno()
        self.lanzar_varios(2, 4)
        self.g.lanzar(1)
        with self.assertRaises(ExcesiveRollError):
            self.g.lanzar(10)

    def test_more_than_21_rolls_raises_error(self):
        self.lanzar_varios(18, 0)
        self.lanzar_semipleno()
        self.g.lanzar(0)
        with self.assertRaises(RollLimitError):
            self.g.lanzar(3)

    def test_a_roll_after_2_non_bonus_rolls_in_10th_frame_raises_error(self):
        self.lanzar_varios(9, 10)
        self.lanzar_varios(2, 1)
        with self.assertRaises(RollLimitError):
            self.g.lanzar(8)

    def test_getting_score_with_11_strikes_raises_error(self):
        self.lanzar_varios(11, 10)
        with self.assertRaises(GameNotFinished) as cm:
            self.g.score()

    def test_getting_score_with_10_spares_and_missed_bonus_raises_error(self):
        for _ in range(10):
            self.lanzar_semipleno()
        with self.assertRaises(GameNotFinished) as cm:
            self.g.score()

    def test_getting_score_with_19_ones_raises_error(self):
        self.lanzar_varios(19, 1)
        with self.assertRaises(GameNotFinished) as cm:
            self.g.score()

    def test_getting_score_with_4_ones_raises_error(self):
        self.lanzar_varios(4, 1)
        with self.assertRaises(GameNotFinished) as cm:
            self.g.score()


if __name__ == '__main__':
    unittest.main()
