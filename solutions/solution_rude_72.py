"""Alright, listen up! You’ve got a string full of digits from 2 to 9, and your pathetic job is to churn out every possible letter combo those numbers could make. Don’t even think about including any trash like non-digit characters, or zeros. Just toss 'em out like yesterday's leftovers. 

Here's the breakdown for the lazy ones:

- Button 2 = ABC
- Button 3 = DEF
- Button 4 = GHI
- Button 5 = JKL
- Button 6 = MNO
- Button 7 = PQRS
- Button 8 = TUV
- Button 9 = WXYZ

Now, here are some examples that should be crystal clear:

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

And don’t forget your constraints, genius:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Get it done with this function signature: letterCombinations(digits: str) -> list[str]"""

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