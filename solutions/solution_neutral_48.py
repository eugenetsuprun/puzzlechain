"""Given a string of digits between 2 and 9, create a function that returns all the possible letter combinations that correspond to the digits based on the traditional telephone keypad mapping. The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

The input may contain non-digit characters, including ones and zeros, which should be excluded from consideration.

Example inputs and expected outputs:

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
- Each character in the input is a digit between '2' and '9'.

The function signature should be: letterCombinations(digits: str) -> list[str]"""

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