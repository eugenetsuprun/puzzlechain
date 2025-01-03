"""Urgently tackle this coding challenge! You need to develop a function that takes a string of digits from 2 to 9 and returns all possible letter combinations that these digits could represent—just like the classic telephone keypad! 

Be aware that the input string may contain non-digit characters, ones, or zeros. You MUST filter these out before processing!

Here's the critical mapping you need to remember:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Your function should handle various input scenarios, such as:
1. An empty string.
2. A string with valid digits.
3. A string with noise (like symbols or zeros).

Examples of inputs and expected outputs:
- Input: "23" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
- Input: "" → Output: []
- Input: "2" → Output: ["a","b","c"]
- Input: "12*30" → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Make sure to strictly adhere to these constraints:
- 0 <= digits.length <= 4
- digits[i] must be a digit in the range ['2', '9'].

The function signature you need to implement is: `letterCombinations(digits: str) -> list[str]`.

Time is of the essence—get started NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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