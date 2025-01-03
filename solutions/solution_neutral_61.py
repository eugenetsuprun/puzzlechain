"""Given a string that includes digits from 2 to 9, the task is to return all possible letter combinations represented by those numbers according to the traditional telephone keypad mapping outlined below.

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as the digits 1 and 0, which should be disregarded in the output. 

Examples:
1. If the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the output should be [].
3. If the input is "2", the output should be ["a", "b", "c"].
4. If the input is "12*30", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Constraints:
- The length of the input string will be between 0 and 4.
- Each character in the string will be a digit from '2' to '9'.

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
    
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    combinations = []
    backtrack(0, "")
    return combinations