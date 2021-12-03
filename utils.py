import random
import numpy as np

def convert_to_electable(candidate, rank):
    if candidate in rank:
        idx = rank.index(candidate)
        rank.pop(idx)
        rank.insert(0, candidate)
    return rank

def generate_ranks(number):

    electability = list(range(1, number+1))
    random.shuffle(electability)
    for i in range(len(electability)):
        electability[i] = 1/(electability[i]**2)

    proportion = 0.35
    truthful = []
    deviation = []
    for i in range(100):
        favorability = [random.random() for i in electability]
        truthful.append([x + 1 for x in np.argsort(favorability)][::-1])
        if random.random() < proportion:
            rank = [favorability[i]*electability[i] for i in range(number)]
            deviation.append([x + 1 for x in np.argsort(rank)][::-1])
        else:
            deviation.append([x + 1 for x in np.argsort(favorability)][::-1])
    return [truthful, deviation]

def calculate_stats(winner, truthful):
    total = 0
    count = 0
    last_count = 0
    for i in truthful:
        if winner in i:
            count += 1
            rank = i.index(winner) + 1
            total += rank
            if rank == len(i):
                last_count += 1
    avg = float(total)/count
    last_prop = float(last_count)/len(truthful)
    return [avg, last_prop]




