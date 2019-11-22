from modules.list_generator import generate_random_list
from modules.sorter import bogo_sort


def main():
    num_range = 10
    list_size = 10

    orig_list = generate_random_list(num_range, list_size)
    print('Generated list:', orig_list)

    sorted_list = bogo_sort(orig_list)
    print('Sorting completed! Sorted list is:', sorted_list)


if __name__ == "__main__":
    main()
