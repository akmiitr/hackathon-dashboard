from aenum import Enum


class ProblemDifficultyLevels(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


DEFAULT_PROBLEMS_TO_SHOW_ON_DASHBOARD = 5
