"""Given a string that contains digits from 2 to 9, return all possible letter combinations corresponding to the digits. The mappings of the digits to letters are as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as digits 0 and 1, should be ignored in the processing.

Example 1:

Input: digits = "23"  
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:

Input: digits = ""  
Output: []

Example 3:

Input: digits = "2"  
Output: ["a", "b", "c"]

Example 4:

Input: digits = "12*30"  
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Constraints:

- The length of the digits string is between 0 and 4.
- Each character in the string is a digit within the range of ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    backtrack(0, "")
    return combinations