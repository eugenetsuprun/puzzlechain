"""Please create a function that takes a string consisting of digits from 2 to 9 and returns all possible letter combinations corresponding to those digits, similar to how letters are mapped on a telephone keypad. Kindly ensure that any non-digit characters, including ones and zeros, are filtered out before processing.

For reference, here is the mapping of digits to letters:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

To illustrate your solution, consider the following examples:

1. If the input is "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the output should be [].
3. For an input of "2", you would return ["a", "b", "c"].
4. If the input is "12*30", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Please ensure that the constraints are respected, where the length of the input string can range from 0 to 4, and that each digit is in the range ['2', '9'].

The function signature to use is: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations