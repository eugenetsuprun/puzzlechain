"""Please consider the following task: You are to take a string that contains digits ranging from 2 to 9 and return all possible letter combinations that the input number could represent. You are welcome to return the results in any order.

For your reference, here is the mapping of digits to letters, akin to the buttons on a telephone:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may also contain non-digit characters, as well as ones and zeros. You are kindly asked to filter these out.

For example, here are a few inputs and their expected outputs:

1. If the input is "23", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
2. If the input is an empty string, the expected output is [].
3. If the input is "2", the expected output is ["a", "b", "c"].
4. If the input is "12*30", the expected output is ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Please be mindful of the following constraints:

- The length of the input string will be between 0 and 4.
- Each character in the input string will be a digit in the range of ['2', '9'].

The function signature for this task is: letterCombinations(digits: str) -> list[str]"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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