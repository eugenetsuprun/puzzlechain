"""URGENT: You need to tackle a critical coding challenge! Given a string filled with digits from 2-9, your immediate task is to return every possible letter combination these numbers could represent. Remember, this is based on the classic telephone keypad mapping!

Here's the breakdown:

- Button 2 corresponds to ABC
- Button 3 corresponds to DEF
- Button 4 corresponds to GHI
- Button 5 corresponds to JKL
- Button 6 corresponds to MNO
- Button 7 corresponds to PQRS
- Button 8 corresponds to TUV
- Button 9 corresponds to WXYZ

IMPORTANT: Filter out any non-digit characters, as well as any occurrences of ones or zeros!

You MUST provide outputs following these examples for clarity:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints you must adhere to:
0 <= digits.length <= 4
Each digit in digits is guaranteed to be in the range ['2', '9'].

Your function signature should be as follows: letterCombinations(digits: str) -> list[str]

Time is of the essence! Get coding NOW!"""

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