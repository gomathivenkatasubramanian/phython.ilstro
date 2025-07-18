from itertools import combinations

def find_even_sum_subsets(data):
   
    even_subsets = []
    for i in range(len(data) + 1):
        for subset in combinations(data, i):
            if sum(subset) % 2 == 0:
                even_subsets.append(list(subset))
        return even_subsets

