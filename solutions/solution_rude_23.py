"""Alright, listen up! You’ve got a string full of those pesky digits from 2 to 9, and it’s your job to spit out all the possible letter combos those numbers can make. Think of it like those lame old phone keypads that used to exist. 

Here’s the breakdown for the digits:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and don’t worry about any non-digit nonsense, ones, or zeros—just toss those out like yesterday's trash.

Check this out:
Example 1:
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: ""
Output: []

Example 3:
Input: "2"
Output: ["a","b","c"]

Example 4:
Input: "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Now, remember, the length of that digit string can only be between 0 and 4, and make sure those characters in your input are digits from 2 to 9. 

Your task? Write a function called `letterCombinations(digits: str) -> list[str]` and make it happen. Don’t screw it up!"""

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