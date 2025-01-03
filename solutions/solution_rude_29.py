"""Alright, listen up! You’ve got a string that’s supposed to have digits from 2 to 9. Your job? Figure out all the letter combos those numbers can create, just like the junk on old-school phone buttons. Toss out any non-digit trash, including ones and zeros, because who wants that nonsense?

Here’s the stupid digit-letter mapping you’ve got to work with:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Got it? Now quit whining. 

Here are some examples to guide you, but don’t get too comfy. 

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

You better handle it. Constraints are simple: the length of digits can be between 0 and 4, and only digits from '2' to '9' are allowed. Your function signature? It’s: letterCombinations(digits: str) -> list[str].

Now get to work!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
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
        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations