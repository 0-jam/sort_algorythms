import argparse
from time import sleep

from modules.sorter import shuffle

# All characters on the keyboard as integers
CHARS = list(range(32, 128)) + [8, 9, 10]


def generate_text(gen_size=100):
    generated_text = ''

    for _ in range(gen_size):
        generated_text += chr(shuffle(CHARS)[0])

    return generated_text


def main():
    parser = argparse.ArgumentParser(description='The text generator based on infinite monkey theorem')
    parser.add_argument('-g', '--gen_size', type=int, default=1000, help='The number of characters to generate (default: 1000)')
    parser.add_argument('-w', '--wait', type=float, default=0, help='Wait time during generation (default: no wait)')
    parser.add_argument('--infinity', action='store_true', default=False, help='Infinity mode (Ctrl+C to stop)')
    args = parser.parse_args()

    try:
        while args.infinity:
            print(chr(shuffle(CHARS)[0]), end='', flush=True)
            sleep(args.wait)
        else:
            gen_size = args.gen_size

            for _ in range(gen_size):
                print(chr(shuffle(CHARS)[0]), end='', flush=True)
                sleep(args.wait)
    except KeyboardInterrupt:
        print()
        print('Aborted!')

    print()


if __name__ == "__main__":
    main()
