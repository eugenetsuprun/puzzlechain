"""Alright, listen up! You’ve got a string packed with digits from 2 to 9, and your mission is to whip up all the possible letter combos those numbers could spit out. Just like how they did it on those ancient phone buttons that nobody uses anymore. 

Here’s the breakdown for the lazy ones:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and do us a favor: if you see any non-digit clutter, like ones or zeros, just toss them out. We’re not here to play with trash!

Check these examples if you need a clue:
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

You’ve got some constraints to deal with too:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

The function you need to crank out is: letterCombinations(digits: str) -> list[str] 

Now get to it, genius!"""

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