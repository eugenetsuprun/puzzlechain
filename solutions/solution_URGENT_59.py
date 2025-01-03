"""You must tackle this urgent coding challenge NOW! Given a string comprised of digits from 2-9, you need to urgently return ALL possible letter combinations that the number can represent! Get ready to use the classic telephone button mapping provided below:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

Remember, your input may also contain non-digit characters, zeros, or ones—so filter those out IMMEDIATELY!

Here are some examples to guide you:

Example 1:  
Input: digits = "23"  
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:  
Input: digits = ""  
Output: []

Example 3:  
Input: digits = "2"  
Output: ["a", "b", "c"]

Example 4:  
Input: digits = "12*30"  
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Keep in mind the constraints:  
0 <= digits.length <= 4  
digits[i] is a digit within the range ['2', '9'].

Your mission starts now! Implement the function: letterCombinations(digits: str) -> list[str] and solve this task with the utmost urgency!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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