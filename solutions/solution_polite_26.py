"""Given a string that contains digits ranging from 2 to 9, you are kindly requested to return all possible letter combinations that each number could represent. You may present the results in any order that you find suitable.

Below is a helpful mapping of digits to their corresponding letters, reminiscent of those found on telephone keypads:

- Button 2: ABC  
- Button 3: DEF  
- Button 4: GHI  
- Button 5: JKL  
- Button 6: MNO  
- Button 7: PQRS  
- Button 8: TUV  
- Button 9: WXYZ  

Please note that the input number may include non-digit characters, such as ones or zeros. Kindly filter these out as you process the input.

For your reference, here are a few examples:

1. Input: digits = "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: digits = ""  
   Output: []

3. Input: digits = "2"  
   Output: ["a","b","c"]

4. Input: digits = "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Please consider the constraints that apply:

- The length of the digits string will be between 0 and 4.
- Each character in digits will be a digit within the range ['2', '9'].

The function signature for your implementation is: letterCombinations(digits: str) -> list[str]"""

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
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
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