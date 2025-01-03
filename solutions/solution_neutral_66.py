"""Given a string that consists of digits ranging from 2 to 9, the task is to return all possible letter combinations that the number could represent, in any order. Each digit corresponds to a set of letters similar to the layout found on telephone keypads:

- 2 maps to ABC
- 3 maps to DEF
- 4 maps to GHI
- 5 maps to JKL
- 6 maps to MNO
- 7 maps to PQRS
- 8 maps to TUV
- 9 maps to WXYZ

Any non-digit characters, including 1s and 0s, should be filtered out from the input string.

Here are some examples:

1. For an input of "23", the output should be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. An empty input string should return: [].
3. An input of "2" should yield: ["a", "b", "c"].
4. For an input of "12*30", the output should again be: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The constraints are as follows:
- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit within the range of ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations