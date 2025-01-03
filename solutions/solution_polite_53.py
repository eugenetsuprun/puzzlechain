"""You are invited to tackle a coding task that involves generating letter combinations from a string of digits. Please consider the following:

You will be provided with a string containing digits ranging from 2 to 9. Your objective is to return all the possible letter combinations that these digits could represent, following the mapping provided below, which mirrors the letter assignments found on telephone buttons:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as ones or zeros. Kindly filter those out before proceeding. 

For your reference, here are some examples of inputs and their corresponding outputs:

- Example 1:
  - Input: digits = "23"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

- Example 2:
  - Input: digits = ""
  - Output: []

- Example 3:
  - Input: digits = "2"
  - Output: ["a","b","c"]

- Example 4:
  - Input: digits = "12*30"
  - Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Please adhere to the constraint that the length of the digits string will be between 0 and 4, with each digit falling within the range of ['2', '9'].

The function signature you should use is: letterCombinations(digits: str) -> list[str]

Best of luck with this engaging challenge!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations