import random
import time


def shuffle(orig_list):
    return random.sample(orig_list, k=len(orig_list))


def bogo_sort(orig_list):
    count = 0
    start_time = time.time()
    sorted_list = sorted(orig_list)

    while True:
        shuffled_list = shuffle(orig_list)
        count += 1
        elapsed_time = time.time() - start_time

        print("list: {}, count: {}, elapsed time: {:.3f}sec".format(shuffled_list, count, elapsed_time), end='\r', flush=True)

        if shuffled_list == sorted_list:
            print('')
            break

    return shuffled_list


def bogo_search(orig_list, query=1):
    count = 0
    start_time = time.time()

    while True:
        found = shuffle(orig_list)[0]
        count += 1
        elapsed_time = time.time() - start_time

        print("found: {}, count: {}, elapsed time: {:.3f}sec".format(found, count, elapsed_time), end='\r', flush=True)

        if found == query:
            print('')
            break

    return found
