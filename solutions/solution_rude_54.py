"""You’ve got a string with some digits from 2-9, and you want to figure out all the possible letter combos from those numbers? Really? Fine. Just remember, we're using the telephone button mapping, so don’t mess it up. 

Here's the breakdown, genius:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Oh, and if you think you can slip in some non-digit characters or even a zero, just filter those losers out. 

Get it? 

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

And don’t forget the lovely constraints: 0 <= digits.length <= 4 and digits[i] is a digit in the range ['2', '9']. 

Now, go ahead and write the function: letterCombinations(digits: str) -> list[str]. Good luck, you're gonna need it!"""

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
    digits = ''.join(filter(str.isdigit, digits))  # Filter out non-digit characters
    backtrack(0, "")
    return combinations