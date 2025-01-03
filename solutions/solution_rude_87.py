"""Alright, listen up. You’ve got this string full of digits, 2 through 9. Your job, if you can handle it, is to spit out all the possible letter combos those numbers could represent. The mapping is as follows—like you’ve never seen a phone before:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and yeah, the string might have some useless junk, like ones or zeros—just toss those out. 

Here’s how it goes:

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

You’ve got some constraints here: the length of the digits can’t go over 4, and make sure those digits are from 2 to 9. 

Now go get it done, will you? The function signature you need is: letterCombinations(digits: str) -> list[str]. Don’t mess it up!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    valid_digits = [d for d in digits if d in phone_map]
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations