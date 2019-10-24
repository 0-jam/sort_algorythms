# Sort Algorithms

Various non-pragmatic snippets

## Bogo search

1. Shuffle the list
1. Extract the first element from the shuffled list
1. If the extracted element matches the query, return the extracted element
    - BUG: If the query does not exist in the list, this program will never end

## Monkey text generator

The text generator based on [Infinite monkey theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)

1. Create the list includes all characters on the keyboard
   - Decimal description: `8, 9, 10`, `32` to `127`
   - All printable ASCII characters + backspace (`\b`), horizontal tab (`\t`), line feed (`\n`) and delete (`DEL`)
1. Extract the first element from the shuffled list of characters
1. Convert number to a Unicode character
1. Display converted character
