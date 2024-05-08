class CricketScoreboard:
    def __init__(self, team1, team2, total_overs):
        self.team1 = team1
        self.team2 = team2
        self.total_overs = total_overs
        self.current_over = 0
        self.current_ball = 0
        self.team1_score = 0
        self.team2_score = 0
        self.current_batsman = None
        self.current_bowler = None

    def start_match(self):
        print("Match started between {} and {}".format(self.team1, self.team2))
        print("Total overs per side:", self.total_overs)

    def next_ball(self, runs):
        if self.current_over >= self.total_overs:
            print("Match over!")
            return

        self.current_ball += 1
        if self.current_ball > 6:
            self.current_ball = 1
            self.current_over += 1

        if self.current_over % 2 == 0:
            self.team2_score += runs
        else:
            self.team1_score += runs

        self.display_score()

    def display_score(self):
        print("--------------------------------------------------")
        print("Current Scoreboard:")
        print("{}: {}-{} in {} overs".format(self.team1, self.team1_score, self.team1_score, self.current_over))
        print("{}: {}-{} in {} overs".format(self.team2, self.team2_score, self.team2_score, self.current_over))
        print("--------------------------------------------------")

# Example usage
scoreboard = CricketScoreboard("Team A", "Team B", 5)
scoreboard.start_match()
scoreboard.next_ball(1)
scoreboard.next_ball(2)
scoreboard.next_ball(0)
scoreboard.next_ball(6)
scoreboard.next_ball(4)
scoreboard.next_ball(1)
scoreboard.next_ball(2)
scoreboard.next_ball(1)
