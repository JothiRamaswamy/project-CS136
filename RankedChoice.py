class RankedChoice:

    def __init__(self, candidates, vote_count, preferences, pref_type):
        self.candidates = candidates
        self.vote_count = vote_count
        self.preferences = preferences
        self.pref_type = pref_type

    def determine_winner(self):
        vote_tally = [0] * len(self.candidates)
        candidates_left = list(self.candidates.keys())
        preferences = self.preferences.copy()
        while True:
            for p in range(len(preferences)):
                if len(preferences[p]) == 1:
                    continue
                try:
                    while preferences[p][1] not in candidates_left:
                        preferences[p].pop(1)
                        if len(preferences[p]) == 1:
                            continue
                except:
                    continue
                idx = candidates_left.index(preferences[p][1])
                vote_tally[idx]+=preferences[p][0]
                
            if max(vote_tally) == min(vote_tally):
                return "Tie"
            elif max(vote_tally) > sum(vote_tally)/2:
                idx = vote_tally.index(max(vote_tally))
                winner_idx = candidates_left[idx]
                return self.candidates[winner_idx]
            else:
                idx = vote_tally.index(min(vote_tally))
                candidates_left.pop(idx)
                vote_tally = [0] * len(candidates_left)