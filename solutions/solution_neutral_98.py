"""Given a string that consists of digits from 2 to 9, your task is to return all potential letter combinations that the digits can signify, presented in any order.

The mapping of digits to letters, similar to a telephone keypad, is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 1 and 0, should be removed from the input.

Examples:
1. For an input of "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. For an empty input, the output should be [].
3. For an input of "2", the output should be ["a","b","c"].
4. For an input like "12*30", the output should result in ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Constraints:
- The length of the input string can range from 0 to 4.
- Each character in the input string must be a digit in the range ['2', '9'].

The function signature should be: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 1 and 0
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations