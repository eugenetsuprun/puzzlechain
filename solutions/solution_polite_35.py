"""You are kindly invited to solve a coding challenge that involves generating possible letter combinations from a given string of digits ranging from 2 to 9. The task requires you to consider a mapping of digits to letters similar to those found on telephone buttons, as detailed below:

- Button 2: ABC  
- Button 3: DEF  
- Button 4: GHI  
- Button 5: JKL  
- Button 6: MNO  
- Button 7: PQRS  
- Button 8: TUV  
- Button 9: WXYZ  

Please note that the input string may contain non-digit characters, as well as zeros or ones, which should be filtered out. 

Here are a few examples to guide you:

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

You may find the following constraints useful:  
- 0 <= digits.length <= 4  
- digits[i] is a digit in the range ['2', '9'].  

The function signature is:  
letterCombinations(digits: str) -> list[str]  

Thank you for your effort in tackling this interesting task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    
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