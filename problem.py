from constants import ProblemDifficultyLevels


class Problem:
    def __init__(self, name, score, description, tag, difficulty: ProblemDifficultyLevels):
        self.name = name
        self.score = score
        self.description = description
        self.tag = tag
        self.difficulty = difficulty
        self.problem_solvers = set()
