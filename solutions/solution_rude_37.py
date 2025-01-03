"""Alright genius, here’s the deal: you've got a string filled with digits from 2-9, and your pathetic task is to churn out every possible letter combo these numbers could conjure up. And guess what? You can toss out all the non-digit crap – like zeros and ones – because nobody’s got time for that nonsense.

Here's the breakdown of what each button represents:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Now, don’t come crying to me if you mess this up. Just filter out the junk and return the results in whatever order you feel like. 

Check out these examples if you need a hand (but really, you should know how to do this):

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

Remember, the constraints are simple: keep it between 0 and 4 for the length of digits, and make sure digits[i] is a digit in the range ['2', '9']. 

Get to it, and don’t screw it up. The function you need is: letterCombinations(digits: str) -> list[str]"""

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
    backtrack(0, "")
    return combinations