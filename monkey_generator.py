from modules.sorter import shuffle


def main():
    # All characters on the keyboard as integers
    chars = list(range(32, 128)) + [8, 9, 10]

    gen_size = 1000

    for _ in range(gen_size):
        print(chr(shuffle(chars)[0]), end='')

    print()


if __name__ == "__main__":
    main()
