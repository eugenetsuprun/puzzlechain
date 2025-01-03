"""You have an urgent coding challenge that demands your immediate attention! Your task is to take a string filled with digits ranging from 2 to 9 and return every possible letter combination that those numbers could represent. Here’s the crucial mapping you must follow:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, including ones and zeros, need to be swiftly filtered out! 

Consider the following examples to guide your implementation:

- Input: digits = "23"
  - Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
  
- Input: digits = ""
  - Output: []

- Input: digits = "2"
  - Output: ["a", "b", "c"]

- Input: digits = "12*30"
  - Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Keep in mind the constraints:
- The length of digits is between 0 and 4.
- Each digit must be in the range ['2', '9'].

Your function signature should be: `letterCombinations(digits: str) -> list[str]`

Time is of the essence—get to work and solve this challenge NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations