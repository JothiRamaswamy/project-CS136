import numpy as np

class TwoRound:

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

        if max(vote_tally) > sum(vote_tally):
            idx = vote_tally.index(max(vote_tally))
            return self.candidates[idx]

        rank_order = list(np.argsort(vote_tally))[-2:]
        print(vote_tally)
        final_tally = [0,0]

        for p in range(len(preferences)):
            for i in range(len(preferences[p])):
                if preferences[p][i] in rank_order:
                    idx = rank_order.index(preferences[p][i])
                    final_tally[idx] += 1
                    continue
        print(final_tally, rank_order)
        if final_tally[0] > final_tally[1]:
            return self.candidates[rank_order[0]+1]
        elif final_tally[0] < final_tally[1]:
            return self.candidates[rank_order[1]+1]
        return "Tie"