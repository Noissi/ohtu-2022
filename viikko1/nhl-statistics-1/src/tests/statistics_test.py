import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_exists(self):
        player = self.statistics.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_search_does_not_exist(self):
        player = self.statistics.search("Kuri")

        self.assertEqual(player, None)

    def test_team(self):
        players = self.statistics.team("EDM")
        names = list(map(lambda x: x.name, players))

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_scorers(self):
        players = self.statistics.top_scorers(3)
        names = list(map(lambda x: x.name, players))

        self.assertEqual(names, ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri'])
