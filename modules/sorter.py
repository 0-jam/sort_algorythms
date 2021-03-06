import random
import time
from collections import deque
from copy import deepcopy

from modules.list_generator import random_swap, swap_list


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


# Swap the first element for the last element in orig_list
def swap_lr(orig_list):
    orig_list_dq = deque(orig_list)

    left_end = orig_list_dq.popleft()
    right_end = orig_list_dq.pop()

    orig_list_dq.append(left_end)
    orig_list_dq.appendleft(right_end)

    return list(orig_list_dq)


def stooge_sort(orig_list, l_end, r_end):
    print('list:'.format(orig_list), end='\r')
    if l_end >= r_end:
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


def bozo_sort(orig_list):
    count = 0
    start_time = time.time()
    sorted_list = sorted(orig_list)

    while True:
        random_swap(orig_list)
        count += 1
        elapsed_time = time.time() - start_time

        print("list: {}, count: {}, elapsed time: {:.3f}sec".format(orig_list, count, elapsed_time), end='\r', flush=True)

        if orig_list == sorted_list:
            print('')
            break

    return orig_list


def bozo_search(orig_list, query=1):
    count = 0
    start_time = time.time()
    # Create the deep copy for keeping the original list
    target_list = deepcopy(orig_list)

    while True:
        random_swap(target_list)
        found = target_list[0]
        count += 1
        elapsed_time = time.time() - start_time

        print("found: {}, count: {}, elapsed time: {:.3f}sec".format(found, count, elapsed_time), end='\r', flush=True)

        if found == query:
            print('')
            break

    return found


def slow_sort(orig_list, l_end, r_end):
    print('list:'.format(orig_list), end='\r', flush=True)
    if l_end >= r_end:
        return

    idx_center = int((r_end + l_end) / 2)
    slow_sort(orig_list, l_end, idx_center)
    slow_sort(orig_list, idx_center + 1, r_end)
    if orig_list[idx_center] > orig_list[r_end]:
        swap_list(orig_list, idx_center, r_end)
    slow_sort(orig_list, l_end, r_end - 1)

    return orig_list
