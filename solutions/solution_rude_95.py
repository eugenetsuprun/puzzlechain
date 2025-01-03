"""Alright, genius, here’s the deal. You’ve got this string full of numbers from 2 to 9, and your pathetic job is to figure out all the letter combos that those numbers could represent. Just like those old-school telephone buttons. 

Here’s the mapping for you, in case you’ve forgotten:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and don’t waste my time with any non-digit nonsense, ones, or zeros. Just toss them out like yesterday's trash.

Let’s see some examples for your slow brain:

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

And oh, don’t forget the constraints:  
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].

Now, go ahead and write the function: letterCombinations(digits: str) -> list[str]. Make it snappy!"""

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