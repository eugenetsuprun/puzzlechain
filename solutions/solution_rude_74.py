"""Alright genius, here’s the deal: you’ve got a string full of digits ranging from 2 to 9, and your job is to spit out all those possible letter combos those numbers could represent. Just like the ancient relics called telephones did. 

Here’s the breakdown: 

- Button 2 has ABC 
- Button 3 has DEF 
- Button 4 has GHI 
- Button 5 has JKL 
- Button 6 has MNO 
- Button 7 has PQRS 
- Button 8 has TUV 
- Button 9 has WXYZ 

Oh, and don’t even think about including any pesky non-digit characters, ones, or zeros in your precious input. Just toss them out like yesterday's leftovers. 

Check this out:

Input: digits = "23" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "" 
Output: []

Input: digits = "2" 
Output: ["a","b","c"]

Input: digits = "12*30" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And keep this in mind: 

- You can only deal with strings that are 0 to 4 characters long. 
- The digits you’re allowed to work with are from 2 to 9. 

So, roll up your sleeves and get coding, because the function signature you’re aiming for is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations