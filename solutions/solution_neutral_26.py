"""Given a string composed of digits ranging from 2 to 9, the task is to generate all possible letter combinations that correspond to the provided digits. The output should be returned in any order.

The following digit-to-letter mappings apply:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, zeros, or ones in the input should be ignored.

Examples for clarification:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints to consider:

- The length of the digits string should be between 0 and 4.
- Each character in the string must be a digit from the set ['2', '9'].

The function signature for implementation is: letterCombinations(digits: str) -> list[str]"""

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
    backtrack(0, "")
    return combinations