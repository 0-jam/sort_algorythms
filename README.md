# Sort Algorithms

Various non-pragmatic snippets. These scripts have no benefit for you.

---

1. [Environment](#environment)
1. [Installation](#installation)
1. [Usage](#usage)
   1. [monkey_generator.py](#monkey_generatorpy)
   1. [avg_gen.py](#avg_genpy)
1. [List of implemented sort algorythms](#list-of-implemented-sort-algorythms)
1. [Search algorythms](#search-algorythms)
   1. [Bogo search](#bogo-search)
   1. [Bozo search](#bozo-search)
1. [Text manipulators](#text-manipulators)
   1. [Monkey text generator](#monkey-text-generator)

---

## Environment

- Arch Linux x86_64 (2020/1/30)
- Windows 10 Insider Preview Build 20180
- Python 3.8.5

## Installation

They have no dependency at now

## Usage

- `-h` for more information

### monkey_generator.py

To enable infinite generation mode (`Ctrl + C` to stop),

`$ python monkey_generator.py --infinity`

You can set the number of characters to generate by `-g`, and wait time for each character generation by `-w`.

### avg_gen.py

You can specify length of the list (`-l`), average value (`-a`), and range of values (`-r`).

If you specified `--low`, it will generate the list that has average value lower than `-a` option.

```
python avg_gen.py -l 20 -a 12 -r 30
[1, 3, 23, 23, 18, 25, 22, 8, 12, 7, 8, 29, 17, 15, 25, 20, 14, 22, 11, 27]
```

## List of implemented sort algorythms

- Bogosort
- Bozo sort
- Stooge sort
- Slow sort

## Search algorythms

### Bogo search

1. Shuffle the list
1. Extract the first element from the shuffled list
1. If the extracted element matches the query, return the extracted element
    - BUG: If the query does not exist in the list, this program will never end

### Bozo search

1. Swap randomly chosen element for another randomly chosen element in the list
1. Do the same thing as [bogo search](#bogo-search)

## Text manipulators

### Monkey text generator

The text generator based on [Infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

1. Create the list includes all characters on the keyboard
   - Decimal description: `8, 9, 10`, `32` to `127`
   - All printable ASCII characters + backspace (`\b`), horizontal tab (`\t`), line feed (`\n`) and delete (`DEL`)
1. Extract the first element from the shuffled list of characters
1. Convert number to a Unicode character
1. Display converted characters
