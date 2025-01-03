"""Alright, genius, listen up. You’ve got a string of digits from 2 to 9, and your job is to figure out all the possible letter combos those numbers can make—just like how we used to dial our pals back in the Stone Age. Here’s the deal: 

Button 2 gives you ABC, Button 3 gives you DEF, and so on. You can’t mix in any non-digit nonsense, so toss out any ones or zeros like yesterday’s garbage. 

Here are some examples to help your brain:

- If you get "23", you better spit out ["ad","ae","af","bd","be","bf","cd","ce","cf"].
- An empty input? Just give back []—easy peasy.
- For "2", don’t screw it up; the answer is ["a","b","c"].
- And if you see "12*30", filter out the junk and come back with ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Now, remember these rules: the string should have a length between 0 and 4, and it must only contain digits from 2 to 9. Your magic function signature for this disaster is: letterCombinations(digits: str) -> list[str]. Now get to it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
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