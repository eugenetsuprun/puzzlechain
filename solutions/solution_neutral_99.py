"""Given a string of digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to those digits, based on the traditional phone keypad mapping. The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

It is important to filter out any non-digit characters, including ones and zeros.

Examples to consider:

1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. An input of "" should return an empty list: [].
3. For the input "2", the expected output is ["a", "b", "c"].
4. With an input of "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to note:

- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit in the inclusive range ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

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