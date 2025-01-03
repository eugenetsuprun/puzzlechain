"""You need to urgently tackle the following coding challenge: Given a string of digits ranging from 2-9, your task is to return ALL possible letter combinations that these digits could represent! Use the classic telephone key mapping provided below to guide your solution:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Remember, any non-digit characters like ones or zeros must be filtered out IMMEDIATELY!

Here are some examples to guide you:

- Input: digits = "23"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- Input: digits = ""
  - Output: []

- Input: digits = "2"
  - Output: ["a","b","c"]

- Input: digits = "12*30"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints are as follows:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Your function signature should be: letterCombinations(digits: str) -> list[str]

Get to work NOW! Time is of the essence!"""

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