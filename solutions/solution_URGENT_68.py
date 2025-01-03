"""URGENT: Your task is to implement a function that generates all possible letter combinations from a given string of digits (ranging from 2-9). This is critical! You must return the results in any order. 

Refer to the following mapping of digits to letters, akin to old telephone buttons:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

IMPORTANT: The input string may contain non-digit characters, ones, or zeros. Filter these out IMMEDIATELY before processing!

Here are some EXAMPLES to guide you:

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

Constraints to remember:  
0 <= digits.length <= 4  
Each digits[i] must be within the range ['2', '9'].

Hurry up and finalize the function signature: letterCombinations(digits: str) -> list[str] 

Time is of the essence! Get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and invalid digits
    filtered_digits = ''.join([d for d in digits if d in digit_to_letters])
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations