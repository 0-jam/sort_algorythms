from modules.sorter import bogo_search


def main():
    orig_list = range(1000)
    query = 1

    bogo_search(orig_list, query)
    print('Query {} is existing in the list'.format(query))


if __name__ == "__main__":
    main()
