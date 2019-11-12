import random
import time

rng = random.SystemRandom(time.time())


def generate_random_list(num_range=10, list_size=10):
    return [rng.randrange(num_range) for _ in range(list_size)]


# Swap a and b in orig_list
# It changes orig_list
def swap_list(orig_list, a, b):
    orig_list[a], orig_list[b] = orig_list[b], orig_list[a]


def random_swap(orig_list):
    idx_a = rng.randrange(len(orig_list))
    idx_b = rng.randrange(len(orig_list))

    swap_list(orig_list, idx_a, idx_b)
