"""Given a string composed of digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to the digits, based on the traditional mapping like those found on telephone keypads. The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 1 and 0, should be ignored.

Examples to consider:

1. For the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. An input of "" should return [].
3. For the input "2", the output should be ["a", "b", "c"].
4. If the input is "12*30", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints to keep in mind:

- The length of the digits string can range from 0 to 4.
- Each character in the string must be a digit from the range ['2', '9'].

The signature for the function is: letterCombinations(digits: str) -> list[str]"""

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
    
    combinations = []
    backtrack(0, "")
    return combinations