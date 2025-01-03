"""Alright, genius, here’s the deal: you have a string filled with numbers from 2 to 9. Your job is to crank out every possible combination of letters those digits could represent, like some kind of coding wizard. And yeah, toss aside any junk like non-digit characters, zeros, or ones—who needs that? 

Here’s your silly little mapping for reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, if the input looks like this:

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

Just remember the constraints: you can only deal with a string length of up to 4, and those digits better be between 2 and 9. 

Now go ahead and write that function: letterCombinations(digits: str) -> list[str]. Good luck, you’ll need it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
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