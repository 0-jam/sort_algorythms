import random
import time
from modules.list_generator import generate_random_list


def shuffle(list):
    return random.sample(list, k=len(list))


def bogo_sort(list):
    count = 0
    start_time = time.time()
    sorted_list = sorted(list)

    while True:
        shuffled_list = shuffle(list)
        count += 1
        elapsed_time = time.time() - start_time

        print("list: {}, count: {}, elapsed time: {:.3f}sec".format(shuffled_list, count, elapsed_time), end='\r', flush=True)

        if shuffled_list == sorted_list:
            print('')
            break

    return sorted_list


def main():
    num_range = 10
    list_size = 10

    orig_list = generate_random_list(num_range, list_size)
    sorted_list = bogo_sort(orig_list)

    print('Sorting completed! Sorted list is:', sorted_list)


if __name__ == "__main__":
    main()
