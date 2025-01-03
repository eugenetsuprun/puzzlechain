"""Alright genius, here's the deal: you’ve got a string with digits from 2 to 9, and your job is to whip up all the possible letter combos those numbers can represent. Think of it like the old-school phone buttons – you know, the ones everyone used before texting took over?

Here’s the mapping because I know you need it spelled out:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and if you find any non-digit nonsense like ones or zeros in there, just toss those out like yesterday's garbage.

Check out these examples, so you don’t screw it up:

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

And just to make it crystal clear: the length of your digit string can be anywhere from 0 to 4, and those digits better be between '2' and '9'. 

Now get to it and make that function `letterCombinations(digits: str) -> list[str]` do its thing!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
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