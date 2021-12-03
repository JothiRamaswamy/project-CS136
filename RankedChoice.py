class RankedChoice:

    def __init__(self, candidates, vote_count, preferences):
        self.candidates = candidates
        self.vote_count = vote_count
        self.preferences = preferences

    def determine_winner(self):
        vote_tally = [0] * len(self.candidates)
        candidates_left = list(self.candidates.keys())
        prefs = []
        for i in self.preferences:
            temp = []
            for j in i:
                temp.append(j)
            prefs.append(temp)
        while True:
            for p in range(len(prefs)):
                if len(prefs[p]) == 0:
                    continue
                try:
                    while prefs[p][0] not in candidates_left:
                        prefs[p].pop(0)
                        if len(prefs[p]) == 0:
                            continue
                except:
                    continue
                idx = candidates_left.index(prefs[p][0])
                vote_tally[idx]+=1
                
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
