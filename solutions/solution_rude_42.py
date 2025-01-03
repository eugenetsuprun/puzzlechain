"""Alright, genius, here's the deal: you've got a string full of digits from 2-9, and your job is to spit out every possible letter combo those numbers can create. You know, like how we used to text back in the day before smartphones made everyone lazy.

Here’s the breakdown:
- Button 2 = ABC
- Button 3 = DEF
- Button 4 = GHI
- Button 5 = JKL
- Button 6 = MNO
- Button 7 = PQRS
- Button 8 = TUV
- Button 9 = WXYZ

Oh, and if you see any useless junk like non-digit characters, ones, or zeros, just toss them in the trash. Seriously, we don’t need that garbage cluttering up your output.

Here are a few examples to chew on:

1. If you get "23", what do you spit back? ["ad","ae","af","bd","be","bf","cd","ce","cf"]. Easy, right?
2. An empty input? Just return an empty list. Duh.
3. A single digit "2"? Give me ["a","b","c"].
4. And if you stumble upon "12*30", still give me those combos: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Your function should look like this: `letterCombinations(digits: str) -> list[str]`. Now, get to work and stop wasting my time!"""

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
    digits = ''.join(filter(str.isdigit, digits))  # Filter out non-digit characters
    backtrack(0, "")
    return combinations