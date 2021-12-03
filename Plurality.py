class Plurality:

    def __init__(self, candidates, vote_count, preferences):
        self.candidates = candidates
        self.vote_count = vote_count
        self.preferences = preferences

    def determine_winner(self):
        vote_tally = [0] * len(self.candidates)
        preferences = self.preferences.copy()
        for p in range(len(preferences)):
            try:
                vote_tally[preferences[p][0]-1] += 1
            except:
                continue

        print(vote_tally)
        idx = vote_tally.index(max(vote_tally))
        return self.candidates[idx+1]