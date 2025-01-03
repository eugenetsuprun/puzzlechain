"""Please consider the following task: Given a string that contains digits from 2 to 9, your objective is to return all possible letter combinations that the sequence of numbers could represent. You may present the results in any order you find suitable.

To assist you, a mapping of digits to letters that resemble those found on telephone keypads is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

It is important to note that the input may include non-digit characters, as well as instances of the digits zero or one. Kindly be sure to filter these out as you work on the task.

For your reference, here are a few examples to consider:

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

As a gentle reminder, the following constraints apply:
- The length of the digits string must be between 0 and 4.
- Each character in the string must be a digit within the range of '2' to '9'.

The function signature you should use for this task is: letterCombinations(digits: str) -> list[str] 

Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and digits 0 and 1
    filtered_digits = ''.join([d for d in digits if d in digit_to_char])
    
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