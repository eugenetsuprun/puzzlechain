"""You are kindly requested to write a function that takes a string of digits ranging from 2 to 9 and returns all possible letter combinations that these digits could represent. Please ensure to return the results in any order you find suitable.

For your reference, here is the mapping of digits to corresponding letters, similar to what is found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Additionally, please note that the input number may contain non-digit characters, such as ones and zeros, which you should filter out.

Here are some examples to illustrate the expected input and output:

Example 1:
- Input: digits = "23"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
- Input: digits = ""
- Output: []

Example 3:
- Input: digits = "2"
- Output: ["a","b","c"]

Example 4:
- Input: digits = "12*30"
- Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Please ensure that the function adheres to the following constraints:
- The length of the input string will be between 0 and 4.
- Each character in the string must be a digit from the range ['2', '9'].

The function signature should be: letterCombinations(digits: str) -> list[str]

Thank you for your attention to detail!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
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