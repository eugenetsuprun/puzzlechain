"""Please consider the following coding task: 

You are asked to take a string that contains digits from 2 to 9, and your objective is to return all possible letter combinations that these numbers could represent. You may present your answer in any order you prefer.

For your reference, here is the mapping of digits to letters, similar to the layout found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input number may also contain non-digit characters, such as ones or zeros. We kindly ask that you filter those out accordingly.

Here are a few examples to illustrate the task:

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

You may also want to keep in mind the following constraints:

- The length of the digits string can range from 0 to 4.
- Each character in the digits string must be a digit within the range ['2', '9'].

The function signature you should use is: letterCombinations(digits: str) -> list[str] 

Thank you for your consideration, and best of luck with your solution!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations