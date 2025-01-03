"""Urgent task at hand! We need to tackle a coding challenge that involves generating all possible letter combinations from a string of digits ranging from 2 to 9! 

Your mission is to implement a function that will sift through the input string, filtering out any non-digit characters, ones, or zeros before mapping the valid digits to their corresponding letters. 

Here’s the mapping for reference: 
- Button 2: ABC 
- Button 3: DEF 
- Button 4: GHI 
- Button 5: JKL 
- Button 6: MNO 
- Button 7: PQRS 
- Button 8: TUV 
- Button 9: WXYZ 

Make sure to return the letter combinations in any order. Remember, the function signature is: `letterCombinations(digits: str) -> list[str]`. 

Time is of the essence! Here are a few examples to guide your implementation:

1. **Input:** digits = "23" 
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = "" 
   **Output:** []

3. **Input:** digits = "2" 
   **Output:** ["a","b","c"]

4. **Input:** digits = "12*30" 
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

We have constraints to keep in mind: 
- 0 <= digits.length <= 4 
- digits[i] is a digit in the range ['2', '9'].

Focus and act fast! The clock is ticking!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters and map digits to letters
    valid_digits = [d for d in digits if d in digit_to_letters]
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        letters = digit_to_letters[valid_digits[index]]
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations