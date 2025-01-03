"""You are kindly requested to devise a solution for a coding challenge that involves generating all possible letter combinations from a given string of digits ranging from 2 to 9. The output should present the combinations in any order, and you may find the following digit-to-letter mapping helpful:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, zeros, or ones, and it would be best to filter these out. 

Here are a few examples to illustrate the expected behavior:

1. If the input is "23", you should return: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. For an empty input string, such as "", the output should understandably be: [].
3. Given the input "2", the expected output is: ["a", "b", "c"].
4. If the input is "12*30", the result should align with the valid digits and return: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Please ensure that your solution adheres to the constraints where the length of the digits can range from 0 to 4 and each digit falls within the specified range from '2' to '9'.

The function signature for your implementation should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    valid_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not valid_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(valid_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[valid_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations