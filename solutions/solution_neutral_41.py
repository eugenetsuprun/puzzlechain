"""Given a string that consists of digits from 2-9, the task is to return all possible combinations of letters that the digits could represent, similar to the mapping on a telephone keypad. The digits correspond to the following letters:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

If the string contains any non-digit characters, such as 1s or 0s, these should be ignored.

Examples:

1. For the input "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. An input of "" should yield an output of [].
3. For the input "2", the output should be ["a","b","c"].
4. If the input is "12*30", the output should again be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Constraints to keep in mind include that the length of the input string will be between 0 and 4, and each character in the string will be a digit within the range of '2' to '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

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
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations