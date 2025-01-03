"""Alright, genius, here’s the deal: you've got this string full of digits from 2 to 9, and your job is to whip up all the possible letter combos these numbers can spit out. Return them however you like. 

Here’s the mapping you need to remember, like it’s rocket science or something:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and if you spot any pesky non-digit characters, ones, or zeros in the mix, just toss them out like yesterday's trash.

Check out these examples, not that you’ll need them:

1. Input: digits = "23" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = "" 
   Output: []

3. Input: digits = "2" 
   Output: ["a","b","c"]

4. Input: digits = "12*30" 
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And don’t forget the rules: your string can be anywhere from 0 to 4 characters long, and each character has to be a digit from '2' to '9'. 

Now, get to it! The function signature you need to use is: letterCombinations(digits: str) -> list[str]."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones or zeros
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations