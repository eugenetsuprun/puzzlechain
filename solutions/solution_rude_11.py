"""Alright genius, listen up. You’ve got this string packed with digits from 2 to 9, and your job is to spit out all the possible letter combinations these numbers can create. You know, like the old-school phone buttons? Yeah, those.

Here’s the breakdown for your lazy brain:

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

Oh, and if you see any non-digit nonsense, or those useless zeros and ones, just toss them in the trash. You don’t need that clutter.

Now, get cracking with these examples:

1. If you input "23", you better output ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. An empty input? Fine, you get []. 
3. Just a "2"? Well, that's ["a","b","c"] for you.
4. And for "12*30"? You’re still churning out ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Keep in mind: the digits are capped at 4 in length, and they better be between '2' and '9'. 

Now, stop wasting time and get to it. The function signature you’ll use is: letterCombinations(digits: str) -> list[str]. Go!"""

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