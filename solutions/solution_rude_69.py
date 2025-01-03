"""Alright genius, listen up. You’ve got this string of digits from 2-9, and your job is to spit out all the letter combos these numbers could possibly represent, just like those old-school phone buttons. Here’s the deal:

2 maps to ABC, 3 maps to DEF, 4 maps to GHI, and so on. If you see any non-digit junk, like ones or zeros, just toss those out like yesterday's trash. 

Let’s say you get this input: "23". You better come back with something like ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. If the input is empty, just give me an empty list. If it’s "2", I want ["a", "b", "c"]. And if you get stuck with something stupid like "12*30", still give me the right combos for the digits that matter.

Oh, and keep it simple: the length of this string can be anywhere from 0 to 4, and remember, it only has digits between '2' and '9'. 

Put your thinking cap on and show me what you’ve got. The function you’re working on is: letterCombinations(digits: str) -> list[str]. Now go make it happen!"""

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
    digits = ''.join(filter(str.isdigit, digits))  # Filter out non-digit characters
    for digit in digits:
        if digit < '2' or digit > '9':
            return []  # Return empty if there's an invalid digit
    
    backtrack(0, "")
    return combinations