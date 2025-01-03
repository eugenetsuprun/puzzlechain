"""URGENT: You need to tackle a critical coding challenge right away! Given a string composed of digits ranging from 2-9, your task is to return ALL possible letter combinations that these numbers could represent. Use the standard mapping from telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: Non-digit characters, as well as ones and zeros, must be filtered out of the input string. 

Here are some examples for reference:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Remember, constraints are as follows:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature should be: letterCombinations(digits: str) -> list[str].

Time is of the essence! Get started immediately!"""

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