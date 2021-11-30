
class Borda:

    def __init__(self, candidates, vote_count, preferences, pref_type):
        self.candidates = candidates
        self.vote_count = vote_count
        self.preferences = preferences
        self.pref_type = pref_type

    def determine_winner(self):
        vote_tally = [0] * len(self.candidates)
        preferences = self.preferences.copy()
        for p in range(len(preferences)):
            for i in range(1, len(preferences[p])):
                try:
                    vote_tally[preferences[p][i]-1] += float(preferences[p][0])*(1/i)
                except:
                    print(preferences[p][i], len(vote_tally))

        idx = vote_tally.index(max(vote_tally))
        return self.candidates[idx+1]
        