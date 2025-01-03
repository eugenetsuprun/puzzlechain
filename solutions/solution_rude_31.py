"""Alright genius, here's the deal: you've got a string filled with digits from 2 to 9 – don't even think about any of those pesky non-digits or zeros mucking things up. Your mission, should you choose to accept it (but seriously, you better), is to spit out all the possible letter combos those numbers can create, just like what you’d find on a phone keypad. 

Here’s the cheat sheet for you:

- 2 = ABC
- 3 = DEF
- 4 = GHI
- 5 = JKL
- 6 = MNO
- 7 = PQRS
- 8 = TUV
- 9 = WXYZ

You’ve got a couple of examples to guide your clueless brain:

1. Input: "23" should give you: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" means you get to output: []
3. Input: "2" gives you: ["a","b","c"]
4. Input: "12*30" should clean up nicely to: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep in mind, your input can be a maximum of 4 characters, each between 2 and 9. Now, stop wasting time and use this signature to get it done: `letterCombinations(digits: str) -> list[str]`. Get cracking!"""

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
    backtrack(0, "")
    return combinations