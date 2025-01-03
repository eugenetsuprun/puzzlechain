"""Given a string consisting of digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to the digits, similar to the mapping on a telephone keypad. The mapping is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be ignored.

Here are some examples to illustrate the expected input and output:

Example 1:
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a","b","c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints for the input are as follows:
- The length of the digits string can range from 0 to 4.
- Each character in the string is guaranteed to be a digit within the range ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

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