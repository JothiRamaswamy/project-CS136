class Plurality:

    def __init__(self, candidates, vote_count, preferences, pref_type):
        self.candidates = candidates
        self.vote_count = vote_count
        self.preferences = preferences
        self.pref_type = pref_type

    def determine_winner(self):
        vote_tally = [0] * len(self.candidates)
        preferences = self.preferences.copy()
        for p in range(len(preferences)):
            try:
                vote_tally[preferences[p][1]] += preferences[p][0]
            except:
                continue

        idx = vote_tally.index(max(vote_tally))
        return self.candidates[idx]