"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations that the digits could represent. The mapping of digits to letters corresponds to the traditional telephone keypad layout.

The mappings are as follows:
- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be ignored in the processing.

Example scenarios include:
1. For the input "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string "", then the output should be [].
3. For the input "2", the expected output is ["a","b","c"].
4. In the case of the input "12*30", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Constraints to consider:
- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit within the range ['2', '9'].

The function signature to implement is: letterCombinations(digits: str) -> list[str]"""

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
    backtrack(0, "")
    return combinations