"""Alright genius, listen up! You’ve got this string packed with digits from 2 to 9, and your job is to whip up all the possible letter combos those numbers could spit out. Just like your old-school phone buttons — remember those? 

Here’s the breakdown: 

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and if you see any pesky non-digit characters, zeros, or ones in there, just toss 'em out like yesterday's trash.

Here are some inputs to chew on:

1. For "23", you should get: ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If it's empty, just return: [].
3. For "2", your output should be: ["a","b","c"].
4. And for "12*30", you better give me: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Just a heads up, your string can be anywhere from 0 to 4 characters long, and those characters better be digits between '2' and '9'. 

Get cracking with this function signature: letterCombinations(digits: str) -> list[str]. Now, no more dilly-dallying!"""

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