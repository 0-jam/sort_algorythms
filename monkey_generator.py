import argparse

from modules.sorter import shuffle


def main():
    parser = argparse.ArgumentParser(description='The text generator based on infinite monkey theorem')
    parser.add_argument('--infinity', action='store_true', default=False, help='Infinity mode (Ctrl+C to stop)')
    args = parser.parse_args()

    # All characters on the keyboard as integers
    chars = list(range(32, 128)) + [8, 9, 10]

    try:
        while args.infinity:
            print(chr(shuffle(chars)[0]), end='', flush=True)
        else:
            gen_size = 1000

            for _ in range(gen_size):
                print(chr(shuffle(chars)[0]), end='', flush=True)
    except KeyboardInterrupt:
        print()
        print('Aborted!')

    print()


if __name__ == "__main__":
    main()
