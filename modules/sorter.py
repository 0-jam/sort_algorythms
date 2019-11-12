import random
import time
from collections import deque


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


# Swap the first element and the last element in orig_list
def swap_lr(orig_list):
    orig_list_dq = deque(orig_list)

    left_end = orig_list_dq.popleft()
    right_end = orig_list_dq.pop()

    orig_list_dq.append(left_end)
    orig_list_dq.appendleft(right_end)

    return list(orig_list_dq)


# Swap a and b in orig_list
# It changes orig_list
def swap_list(orig_list, a, b):
    orig_list[a], orig_list[b] = orig_list[b], orig_list[a]


def stooge_sort(orig_list, l_end, r_end):
    if l_end > r_end:
        return

    if orig_list[l_end] > orig_list[r_end]:
        swap_list(orig_list, l_end, r_end)

    # Length of the partial list that contains last 2/3 elements of the original list
    len_partial = r_end - l_end + 1
    if len_partial > 2:
        # Index of 2/3rd position in the list
        index_23 = round(len_partial * (2 / 3))
        # Index of the first element of the partial list
        index_13 = len_partial - index_23

        stooge_sort(orig_list, l_end=l_end, r_end=r_end - index_13)
        stooge_sort(orig_list, l_end=l_end + index_13, r_end=r_end)
        stooge_sort(orig_list, l_end=l_end, r_end=r_end - index_13)

    return orig_list
