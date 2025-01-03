"""Given a string of digits ranging from 2 to 9, the task is to return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, including ones and zeros, should be filtered out of the input.

Examples:

1. For the input digits = "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. For the input digits = "", the output should be [].
3. For the input digits = "2", the output should be ["a","b","c"].
4. For the input digits = "12*30", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Constraints:
- The length of digits can be between 0 and 4.
- Each digit in digits is in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]"""

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