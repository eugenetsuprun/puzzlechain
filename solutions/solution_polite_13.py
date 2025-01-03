"""Could you please help me with a coding challenge? The task is to take a string composed of digits from 2 to 9 and return all possible letter combinations that these numbers could represent, much like the letters associated with telephone buttons. Below is the mapping for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as the digits one and zero, which should be filtered out.

Here are a few examples to illustrate:

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

Please ensure that the output can be presented in any order and that the constraints are respected:
- The length of the digits can range from 0 to 4.
- Each digit in the input string should be in the range of ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]

Thank you very much for your assistance!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 1 and 0
    filtered_digits = ''.join([d for d in digits if d in phone_map])
    
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