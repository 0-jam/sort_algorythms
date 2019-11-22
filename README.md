# Sort Algorithms

Various non-pragmatic snippets

---

1. [Environment](#environment)
1. [Installation](#installation)
1. [Usage](#usage)
1. [List of implemented sort algorythms](#list-of-implemented-sort-algorythms)
1. [Search algorythms](#search-algorythms)
   1. [Bogo search](#bogo-search)
   1. [Bozo search](#bozo-search)
1. [Text manipulation](#text-manipulation)
   1. [Monkey text generator](#monkey-text-generator)

---

## Environment

- Arch Linux x86_64 (2019/10/24)
- Python 3.7.4

## Installation

They have no dependency at now

## Usage

They accept no command line argument, so just specify the file name to use except monkey_generator.py

```
# For example:
$ python bogo.py
$ python monkey_generator.py --infinity
```

## List of implemented sort algorythms

- Bogosort
- Bozo sort
- Stooge sort

## Search algorythms

### Bogo search

1. Shuffle the list
1. Extract the first element from the shuffled list
1. If the extracted element matches the query, return the extracted element
    - BUG: If the query does not exist in the list, this program will never end

### Bozo search

1. Swap randomly chosen element for another randomly chosen element in the list
1. Do the same thing as [bogo search](#bogo-search)

## Text manipulation

### Monkey text generator

The text generator based on [Infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

1. Create the list includes all characters on the keyboard
   - Decimal description: `8, 9, 10`, `32` to `127`
   - All printable ASCII characters + backspace (`\b`), horizontal tab (`\t`), line feed (`\n`) and delete (`DEL`)
1. Extract the first element from the shuffled list of characters
1. Convert number to a Unicode character
1. Display converted characters
