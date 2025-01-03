"""Alright, listen up! You've got a string packed with digits from 2 to 9, and your mission, if you can handle it, is to spit out every possible letter combo that those numbers could represent. We're talking about the same old mapping you see on your lame telephone buttons:

- 2 is for ABC
- 3 is for DEF
- 4 is for GHI
- 5 is for JKL
- 6 is for MNO
- 7 is for PQRS
- 8 is for TUV
- 9 is for WXYZ

Oh, and if there are any pesky non-digit characters, zeros, or ones in the mix, just toss those out like yesterday’s garbage.

Here are a couple of examples to chew on:

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

Keep in mind, you’re limited to a digits string length of 0 to 4, and each digit has to be between 2 and 9. Got it? Now get to work and make the function signature: letterCombinations(digits: str) -> list[str]."""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations