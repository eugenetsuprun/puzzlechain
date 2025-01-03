"""Alright genius, here’s the deal: you’ve got a string full of digits between 2-9, and you need to whip up all the possible letter combos those numbers can make. Just pretend you’re on a phone and remember what each button does, because I’m not gonna repeat it.

Here’s the mapping – like, you should know this by now:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

And if you stumble upon any non-digit junk, or heaven forbid, some ones or zeros, toss them out like yesterday’s trash. 

Take a gander at these examples, because you’re gonna need to get this right:

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

Keep in mind, the length of those digits is between 0 and 4, and only stick to the digits from '2' to '9', got it? 

Now, get your act together and code this up with the function signature: letterCombinations(digits: str) -> list[str]. Good luck, you’ll need it!"""

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