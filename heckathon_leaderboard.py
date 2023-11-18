from collections import defaultdict

from constants import ProblemDifficultyLevels, DEFAULT_PROBLEMS_TO_SHOW_ON_DASHBOARD
from problem import Problem
from user import User
from datetime import datetime


class HackathonLeaderboardService:

    def __init__(self):
        self.users = {}
        self.problems = {}

    def add_problem(self, name, score, description, tag, difficulty: ProblemDifficultyLevels):
        problem = Problem(name, score, description, tag, difficulty)
        self.problems[name] = problem

    def add_user(self, name, department):
        user = User(name=name, department=department)
        self.users[name] = user

    def solve_problem(self, problem_name, user_name):
        user = self.users.get(user_name)
        if not user:
            raise Exception("User is still not registered")
        problem = self.problems.get(problem_name)
        if not problem:
            raise Exception("Question is yet not added")
        if problem_name in user.solved_problem:
            raise Exception("User has already solved this problem")
        user.solved_problem[problem_name] = datetime.now()
        problem.problem_solvers.add(user_name)

    def fetch_solved_problems(self, user_name):
        user = self.users.get(user_name)
        if not user:
            raise Exception("User is still not registered")
        return list(user.solved_problem.keys())

    def display_leaderboard(self, is_department=True, n=DEFAULT_PROBLEMS_TO_SHOW_ON_DASHBOARD):
        # Get the leaderboard based on the specified criteria
        if is_department:
            leaderboard = defaultdict(int)
            for user in self.users.values():
                leaderboard[user.department] += sum(
                    self.problems[problem_name].score
                    for problem_name in user.solved_problem
                )
        else:
            leaderboard = {
                user.name: sum(self.problems[problem_name].score for problem_name in user.solved_problem)
                for user in self.users.values()
            }
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for i in range(min(n, len(sorted_leaderboard))):
            print(sorted_leaderboard[i])
