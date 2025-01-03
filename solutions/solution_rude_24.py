"""Alright genius, here’s the deal: you’ve got a string full of digits from 2 to 9, and you need to spit out all the possible letter combos those numbers could stand for. Think of it like the letters on a phone keypad, you know, from back in the stone age. 

Here’s the breakdown for you, since I know you need it:

- 2 is for ABC
- 3 is for DEF
- 4 is for GHI
- 5 is for JKL
- 6 is for MNO
- 7 is for PQRS
- 8 is for TUV
- 9 is for WXYZ

Oh, and if there are any pesky non-digit characters, zeros, or ones in that string, just toss them out, will ya?

Here’s what you need to do: 

Input: digits = "23" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "" 
Output: []

Input: digits = "2" 
Output: ["a","b","c"]

Input: digits = "12*30" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And just to keep you on your toes, remember: the length of digits can be anywhere from 0 to 4. You got this? Good. Now get to it. The function signature you’re looking for is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 1 and 0
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations