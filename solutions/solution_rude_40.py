"""Alright, genius, here's the deal. You’ve got a string packed with digits from 2 to 9, and your miserable job is to churn out every possible letter combo those numbers can whip up. Just like a damn old-school phone, you know? 

Here's your stupid mapping:  
Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and don’t waste my time with any non-digit junk, zeroes, or ones. Just toss those losers out. 

Here are some examples to help your tiny brain:  
Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]  

Input: digits = ""  
Output: []  

Input: digits = "2"  
Output: ["a","b","c"]  

Input: digits = "12*30"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]  

Just a heads up:  
0 <= digits.length <= 4  
digits[i] better be a digit in the range ['2', '9'].  

Now get to work! The function signature is: letterCombinations(digits: str) -> list[str]"""

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