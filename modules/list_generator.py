import random
import time

rng = random.SystemRandom(time.time())


def generate_random_list(num_range=10, list_size=10):
    return [rng.randrange(num_range) for _ in range(list_size)]
