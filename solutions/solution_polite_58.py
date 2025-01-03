"""Given a string that may contain digits from 2 to 9, your task is to return all possible letter combinations that the number could represent. The mapping of digits to letters, similar to what you would find on a telephone keypad, is as follows:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain non-digit characters, as well as ones or zeros, which should be filtered out.

Here are a few examples to illustrate the expected output:

1. If the input is "23", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string, the output should be [].
3. If the input is "2", the output should be ["a","b","c"].
4. If the input is "12*30", the output should be ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Please adhere to the following constraints:

- The length of the input string will be between 0 and 4.
- Each character in the input string will be a digit in the range ['2', '9'].

The function signature for your implementation should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail in crafting a solution!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations