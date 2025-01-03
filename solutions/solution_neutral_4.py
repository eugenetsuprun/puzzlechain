"""Given a string composed of digits ranging from 2 to 9, your task is to return all possible letter combinations that the digits could represent according to the mapping traditionally used on telephone keypads. 

The mapping is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Any non-digit characters, as well as the digits 0 and 1, should be ignored. 

Examples to consider:

1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. An input of "" should yield an output of [].
3. For an input of "2", the output should be ["a", "b", "c"].
4. If the input is "12*30", the result should again be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Please note the following constraints:
- The length of the input string can be between 0 and 4.
- Each character within the string must be a digit in the range ['2', '9'].

The required function signature is: letterCombinations(digits: str) -> list[str]"""

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