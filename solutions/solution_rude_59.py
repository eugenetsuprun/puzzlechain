"""Alright genius, listen up! You’ve got this string of digits from 2 to 9, and your pathetic job is to figure out all the possible letter combos those numbers could represent. Yeah, just like on those old-school phone keypads. 

Here’s the deal:

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and if there’s any nonsense in there like non-digits, ones, or zeros? Just toss that garbage out. 

Check out these examples, and try not to screw it up:

Input: "23" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: "" 
Output: []

Input: "2" 
Output: ["a","b","c"]

Input: "12*30" 
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You’ve got some limits here, so don’t push it: 
0 <= length of digits <= 4
And hey, digits must be in the ['2', '9'] range!

So get to it – the function signature is: letterCombinations(digits: str) -> list[str]"""

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