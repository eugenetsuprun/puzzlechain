"""Alright, listen up! You’ve got this string of digits from 2 to 9, and your job is to figure out all the wacky letter combinations those numbers could possibly stand for. Don't overthink it; just treat it like a phone keypad – you know, the one that hasn’t changed since the Stone Age.

Here's the rundown:

- 2 is for ABC
- 3 is for DEF
- 4 is for GHI
- 5 is for JKL
- 6 is for MNO
- 7 is for PQRS
- 8 is for TUV
- 9 is for WXYZ

Oh, and don't waste our time with any non-digit nonsense, zeroes, or ones. Just toss those out like yesterday's leftovers.

Check out these examples to get your brain churning:

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

Now, don’t screw it up. You’ve got these constraints to keep you in line:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Get cracking with this function signature: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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