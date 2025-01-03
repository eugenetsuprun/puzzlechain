"""Please create a function that takes a string of digits ranging from 2 to 9 and returns all possible letter combinations that correspond to those digits, similar to the letters on a telephone keypad. Kindly ensure to ignore any non-digit characters, including any occurrences of zeros or ones. 

To assist you, here is the mapping for reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Here are a few examples to illustrate the expected output:

1. If the input is "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. For an empty input, such as "", the output should be [].
3. If the input is just "2", the output should be ["a","b","c"].
4. If the input includes non-digit characters, such as "12*30", the output should still be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Please adhere to the following constraints:
- The length of the input string can range from 0 to 4.
- Each character in the input should be a digit from '2' to '9'.

The function signature to be used is: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
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