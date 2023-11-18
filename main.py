from heckathon_leaderboard import HackathonLeaderboardService

if __name__ == '__main__':
    hackathon_platform = HackathonLeaderboardService()
    hackathon_platform.add_user("Ashok", "tech")
    hackathon_platform.add_user("Sudarshan", "tech")
    hackathon_platform.add_user("Nitesh", "Manager")
    hackathon_platform.add_user("Sudarshan1", "tech")
    hackathon_platform.add_user("Nitesh1", "Manager")

    hackathon_platform.add_problem(name="Problem1", description="Description1", tag="Tag1", difficulty="easy", score=10)
    hackathon_platform.add_problem(name="Problem2", description="Description2", tag="Tag2", difficulty="medium",
                                   score=20)
    hackathon_platform.add_problem(name="Problem3", description="Description3", tag="Tag1", difficulty="hard", score=30)
    hackathon_platform.add_problem(name="Problem4", description="Description3", tag="Tag1", difficulty="hard", score=30)
    hackathon_platform.add_problem(name="Problem5", description="Description3", tag="Tag1", difficulty="hard", score=30)

    hackathon_platform.solve_problem(user_name="Sudarshan", problem_name="Problem1")
    hackathon_platform.solve_problem(user_name="Nitesh", problem_name="Problem2")
    hackathon_platform.solve_problem(user_name="Ashok", problem_name="Problem3")
    hackathon_platform.solve_problem(user_name="Sudarshan1", problem_name="Problem4")
    hackathon_platform.solve_problem(user_name="Nitesh1", problem_name="Problem5")

    print(hackathon_platform.fetch_solved_problems("Sudarshan"))

    print("Should default items to be displayed on Dashboard")
    hackathon_platform.display_leaderboard(is_department=False)
    print("Custom items to be displayed on Dashboard")
    hackathon_platform.display_leaderboard(is_department=False, n=3)
    print("Next level data")
    hackathon_platform.display_leaderboard(is_department=True, n=3)
