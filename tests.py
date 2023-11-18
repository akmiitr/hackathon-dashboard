import unittest

from constants import ProblemDifficultyLevels
from heckathon_leaderboard import HackathonLeaderboardService


class UnitestCases(unittest.TestCase):

    def test_unregistered_user_try_solve_problem(self):
        hackathon_platform = HackathonLeaderboardService()
        hackathon_platform.add_user("Ashok", "tech")
        hackathon_platform.add_problem(name="Problem1", description="Description1", tag="Tag1",
                                       difficulty=ProblemDifficultyLevels.EASY.value,
                                       score=10)
        try:
            hackathon_platform.solve_problem(user_name="InvalidUser", problem_name="Problem1")
        except Exception as e:
            self.assertTrue(str(e), "User is still not registered")

    def test_registered_user_try_solve_unregisterd_problem(self):
        hackathon_platform = HackathonLeaderboardService()
        hackathon_platform.add_user("Ashok", "tech")
        hackathon_platform.add_problem(name="Problem1", description="Description1", tag="Tag1",
                                       difficulty=ProblemDifficultyLevels.EASY.value,
                                       score=10)
        try:
            hackathon_platform.solve_problem(user_name="Ashok", problem_name="Problem3")
        except Exception as e:
            self.assertTrue(str(e), "Question is yet not added")

    def test_registered_user_try_solve_valid_problem(self):
        hackathon_platform = HackathonLeaderboardService()
        hackathon_platform.add_user("Ashok", "tech")
        hackathon_platform.add_problem(name="Problem1", description="Description1", tag="Tag1",
                                       difficulty=ProblemDifficultyLevels.EASY.value,
                                       score=10)
        hackathon_platform.solve_problem(user_name="Ashok", problem_name="Problem1")
        self.assertTrue("Problem1" in hackathon_platform.problems)
        self.assertTrue("Ashok" in hackathon_platform.users)


if __name__ == '__main__':
    unittest.main()
