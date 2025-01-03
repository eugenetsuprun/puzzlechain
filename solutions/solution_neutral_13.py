"""Given a string of digits ranging from 2 to 9, the task is to return all possible letter combinations that correspond to the input number. The letter mappings for each digit are based on a traditional telephone keypad layout:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be disregarded in the input string.

Examples to consider:

1. For the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the output should be an empty list: [].
3. With the input "2", the expected output is ["a", "b", "c"].
4. For the input "12*30", the output should still be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

The constraints for this function are as follows:

- The length of the input string should be between 0 and 4.
- Each character in the string should be a digit between '2' and '9'.

The function signature is: letterCombinations(digits: str) -> list[str]"""

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
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations