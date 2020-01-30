import random
import time
from statistics import mean

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


def generate_high_avg_list(num_range=10, list_size=10, average=8):
    while True:
        generated_list = generate_random_list(num_range, list_size)

        if mean(generated_list) >= average:
            break

    return generated_list


def generate_low_avg_list(num_range=10, list_size=10, average=6):
    while True:
        generated_list = generate_random_list(num_range, list_size)

        if int(mean(generated_list) <= average):
            break

    return generated_list
