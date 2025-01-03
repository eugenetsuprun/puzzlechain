"""Alright genius, here’s the deal. You’ve got this string with digits between 2 and 9, and your task is to whip up all the possible letter combos those digits can throw at you. Forget about any nonsense like non-digit characters, ones, or zeros—just kick those to the curb.

Here’s the lowdown on what each button corresponds to:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, don’t screw this up. 

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

Here’s your function signature to make it official: 
letterCombinations(digits: str) -> list[str] 

Get to it, and try not to mess it up!"""

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