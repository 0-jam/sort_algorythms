from modules.list_generator import generate_random_list
from modules.sorter import slow_sort


def main():
    orig_list = generate_random_list()
    print('Generated list:', orig_list)

    sorted_list = slow_sort(orig_list, l_end=0, r_end=len(orig_list) - 1)

    print('Sorted list:', sorted_list)


if __name__ == "__main__":
    main()
