class User:

    def __init__(self, name, department):
        self.name = name
        self.department = department
        # The below one should have the problem that has solved and how much time it has taken
        self.solved_problem = {}
