"""Alright, listen up! You’ve got a string of digits from 2 to 9, and your task is to spit out all the possible letter combos those numbers could represent. You know, like how we used to text on those old phones. 

Here’s the mapping if you’ve forgotten:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and if you see any junk characters like ones or zeros, just toss them in the trash. We only want the good stuff.

Check out these examples, if you can handle it:

1. Input: digits = "23" — Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" — Output: []
3. Input: digits = "2" — Output: ["a","b","c"]
4. Input: digits = "12*30" — Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And just so you know, the input won’t be any longer than 4 characters. Got it? Now, get to work with this function signature: letterCombinations(digits: str) -> list[str]. Don’t screw it up!"""

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
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations