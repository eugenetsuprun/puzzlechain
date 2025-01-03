"""Alright genius, listen up. You’ve got this string packed with digits from 2 to 9, and your job is to spit out every possible letter combo those numbers could make. Just treat them like the buttons on a phone, you know, where 2 stands for ABC, 3 for DEF, and so on. 

By the way, if you see any nonsense – like non-digit crap, zeros, or ones – just toss that garbage out. 

Here are some examples in case you need a clue:

Input: digits = "23" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "" 
Output: []

Input: digits = "2" 
Output: ["a","b","c"]

Input: digits = "12*30" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Oh, and by the way, the digit string can’t be longer than 4 characters, and only the digits 2 to 9 are allowed, alright? 

Now get coding with this signature: letterCombinations(digits: str) -> list[str]. Go!"""

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
    
    # Filter out invalid characters
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not digits:
        return []
    
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