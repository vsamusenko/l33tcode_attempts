from collections import Counter

def firstUniqChar(s: str) -> int:
    counter_in = Counter(s)
    single_reps = []
    for letter, reps in counter_in.items():
        if reps == 1:
            single_reps.append(s.find(f'{letter}'))


    if len(single_reps) < 1:
        return -1
    else:
        return min(single_reps)





print(firstUniqChar('aabb'))

