"""You MUST solve this coding task IMMEDIATELY! Given a string containing digits from 2-9, your mission is to return ALL possible letter combinations that the number could represent. You MUST adhere to the typical telephone button mapping below:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

IMPORTANT: The input number may contain non-digit characters, ones, or zeros. These MUST be filtered out before processing!

**EXAMPLES:**  
- Input: digits = "23"  
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]  

- Input: digits = ""  
  Output: []  

- Input: digits = "2"  
  Output: ["a","b","c"]  

- Input: digits = "12*30"  
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]  

**CONSTRAINTS:**  
0 <= digits.length <= 4  
digits[i] is a digit in the range ['2', '9'].  

The function signature you need to implement is: `letterCombinations(digits: str) -> list[str]`

Get to it NOW! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations