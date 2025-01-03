"""Alright genius, here’s the deal. You’ve got this string filled with digits from 2-9, and your job is to whip up all the possible letter combinations those numbers can throw at you. Just like the buttons on a phone, get it? 

Here’s the breakdown if you're too lazy to figure it out: 

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Oh, and if you spot any pesky non-digit characters, ones, or zeros, just toss those out like yesterday’s garbage. 

Check out these examples if you need a clue:

1. Input: digits = "23"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""
   Output: []

3. Input: digits = "2"
   Output: ["a","b","c"]

4. Input: digits = "12*30"
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Oh, and keep in mind the constraints: 0 <= digits.length <= 4, and digits[i] better be a digit from '2' to '9'. 

Your function should look like this: letterCombinations(digits: str) -> list[str]. Now stop slacking and get to it!"""

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