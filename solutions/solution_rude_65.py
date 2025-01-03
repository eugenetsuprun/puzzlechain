"""Alright genius, here’s the deal: you’ve got a string filled with digits from 2 to 9, and you’re supposed to spit out every possible combination of letters these numbers can represent. Yeah, just like those ancient phone keypads. 

Here’s the mapping, because apparently you need it:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and if you find any non-digit junk, or god forbid, a zero or one, just toss that trash out. 

Now, quit whining and get to it. Here are some examples to guide your struggling brain:

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

And just so you know, the digits can be between 0 and 4 characters long, and they better be in the range of ‘2’ to ‘9’. 

You’re going to write a function called `letterCombinations(digits: str) -> list[str]`. Now get to coding and make it snappy!"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations