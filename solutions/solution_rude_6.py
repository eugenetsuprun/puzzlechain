"""Alright genius, listen up! You’ve got a string filled with digits from 2 to 9, and your job is to whip up all the possible letter combinations those numbers could represent. Yeah, the same way your phone does it – you know, back when people actually used phones for calls and not just scrolling through social media.

Here's the breakdown of the digits to letters, in case you need a refresher:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and don’t waste time with any non-digit crap, like zeros or ones. Just filter that junk out.

Check out these examples, in case you need help figuring it out:

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

And remember, the string length can be anywhere from 0 to 4. Got it? Good. Now get to it! The function signature you need is: letterCombinations(digits: str) -> list[str]"""

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