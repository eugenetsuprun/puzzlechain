"""Given a string that contains digits ranging from 2 to 9, the task is to return all potential letter combinations corresponding to those digits. The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, including ones or zeros, should be removed from the string before processing.

Examples to consider:

1. For the input "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string, the output should be [].
3. For the input "2", the output should be ["a","b","c"].
4. For the input "12*30", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

The constraints for the input string are as follows:

- The length of the string can be between 0 and 4.
- Each character in the string must be a digit within the range ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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