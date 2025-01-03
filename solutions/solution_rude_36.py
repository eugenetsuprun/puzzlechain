"""Got a string full of digits from 2 to 9? Good for you! Now, your pathetic little task is to churn out all the letter combos those digits could possibly represent. Just like those old-fashioned phone buttons that no one uses anymore. 

Here's the deal: 

- Button 2 gives you ABC, 
- Button 3 gives you DEF, 
- Button 4 gives you GHI, 
- Button 5 gives you JKL, 
- Button 6 gives you MNO, 
- Button 7 gives you PQRS, 
- Button 8 gives you TUV, 
- Button 9 gives you WXYZ.

Oh, and if you find any useless characters like ones or zeros in there, just toss 'em out like yesterday's trash. 

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

And here are the rules you can't ignore:

0 <= digits.length <= 4
digits[i] is a digit between '2' and '9'. 

Now, go on and write that function: letterCombinations(digits: str) -> list[str] and make it snappy!"""

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