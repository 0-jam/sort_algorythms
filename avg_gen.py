import argparse

from modules.list_generator import generate_high_avg_list, generate_low_avg_list


def main():
    parser = argparse.ArgumentParser(description='The random list generator that guarantees its average value')
    parser.add_argument('-l', '--length', type=int, default=10, help='Length of the generated list')
    parser.add_argument('-a', '--average', type=int, default=8, help='Average value of the generated list')
    parser.add_argument('-r', '--range', type=int, default=10, help='Average value of the generated list')
    parser.add_argument('--low', action='store_true', help='Set generator to the low mode')
    args = parser.parse_args()

    if args.average > args.range:
        raise ValueError('average must be equal or smaller than range')

    if args.average <= 0 or args.range <= 0:
        raise ValueError('average and range must be greater than 0')

    if args.length <= 0:
        raise ValueError('length must be greater than 0')

    if args.low:
        generated_list = generate_low_avg_list(
            num_range=args.range,
            list_size=args.length,
            average=args.average
        )
    else:
        generated_list = generate_high_avg_list(
            num_range=args.range,
            list_size=args.length,
            average=args.average
        )

    print(generated_list)


if __name__ == "__main__":
    main()
