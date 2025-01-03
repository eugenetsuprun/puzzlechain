"""Given a string that contains digits from 2 to 9, your task is to return all possible letter combinations that the string could represent, based on the typical mapping of digits to letters found on telephone keypads. 

The mapping is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Please note that the input string may include non-digit characters, such as 1s or 0s, which should be ignored.

Examples to consider:

1. For an input of "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the output should be [].
3. For an input of "2", the output should be ["a", "b", "c"].
4. An input of "12*30" should yield ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Keep in mind the constraints:
- The length of the input string can be between 0 and 4.
- Each character in the string must be a digit in the range from '2' to '9'.

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
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    backtrack(0, "")
    return combinations