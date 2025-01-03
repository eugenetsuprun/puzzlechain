"""Alright, listen up! You've got a string full of digits from 2 to 9, and your job is to whip up all the possible letter combos those numbers could spell out. Don't even think about throwing in anything else – just the numbers! There's a mapping for these digits, kind of like how your old-school phone used to roll, so get with the program:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and if some annoying non-digit characters or zeros sneak in, just kick 'em to the curb.

Here are a few examples to help your clueless self:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And hey, keep this in mind: the length of your precious digits can be between 0 and 4, and they better be between '2' and '9'. 

Now get crackin’ with this function: letterCombinations(digits: str) -> list[str]. Don't screw it up!"""

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