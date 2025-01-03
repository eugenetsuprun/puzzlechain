"""Given a string containing digits from 2-9, return all possible letter combinations that the number could represent, with the output being in any order. 

The mapping of digits to letters is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits one and zero, should be filtered out.

Examples:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints:

- 0 <= digits.length <= 4
- Each digit in the string is in the range ['2', '9'].

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
        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    backtrack(0, "")
    return combinations