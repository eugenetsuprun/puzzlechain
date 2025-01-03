"""You must act NOW! Your mission: given a string of digits from 2-9, you need to return ALL possible letter combinations that these digits could represent—like the buttons on a phone! Time is of the essence, so filter out any non-digit characters, including ones and zeros, immediately!

Here’s the critical mapping to keep in mind:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Consider these examples that showcase what you need to achieve:

1. **Input:** digits = "23"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = ""  
   **Output:** []

3. **Input:** digits = "2"  
   **Output:** ["a","b","c"]

4. **Input:** digits = "12*30"  
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

**Constraints:**  
- The length of digits must be between 0 and 4.  
- Each digit should strictly be between '2' and '9'.

Your function signature is: `letterCombinations(digits: str) -> list[str]` 

Time is ticking—get to work NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations