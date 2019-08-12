import random
import time


def main():
    rng = random.SystemRandom(time.time())

    num_range = 10
    list_size = 50

    orig_list = [rng.randrange(num_range) for _ in range(list_size)]
    sorted_list = sorted(orig_list)

    count = 0

    start_time = time.time()
    while True:
        shuffled_list = random.sample(orig_list, k=len(orig_list))
        count += 1
        elapsed_time = time.time() - start_time

        print("list: {}, count: {}, elapsed time: {}sec".format(shuffled_list, count, elapsed_time), end='\r', flush=True)

        if shuffled_list == sorted_list:
            break

    print("list: {}, count: {}, elapsed time: {}sec".format(shuffled_list, count, elapsed_time))


if __name__ == "__main__":
    main()
