"""You have an urgent coding challenge to tackle! Your task is to develop a function that takes a string of digits ranging from 2 to 9 and returns all possible letter combinations these numbers can represent. Think of the old phone keypads where each number corresponds to specific letters. 

Here's the mapping:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

You need to ensure that any non-digit characters, as well as the digits 1 and 0, are filtered out from the input. 

To illustrate, consider these examples:
1. Input: "23" → Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
2. Input: "" → Output: []
3. Input: "2" → Output: ["a", "b", "c"]
4. Input: "12*30" → Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Keep in mind the constraints:
- The length of the input string will be between 0 and 4.
- Each character in the string will be a digit from '2' to '9'.

Get ready to implement the function with the following signature: `letterCombinations(digits: str) -> list[str]`. This is a time-sensitive task—let's see your coding skills in action!"""

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