"""Given a string that contains digits from 2 to 9, the task is to return all possible letter combinations that the digits could represent. The mapping of digits to letters is based on the layout of a telephone keypad as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

The input may include non-digit characters such as ones or zeros, which should be ignored.

Example inputs and their expected outputs include:

1. Input: "23"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. Input: ""  
   Output: []

3. Input: "2"  
   Output: ["a","b","c"]

4. Input: "12*30"  
   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Constraints to keep in mind:
- The length of the input string can range from 0 to 4.
- Each character in the string should be a digit from '2' to '9'.

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

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
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations