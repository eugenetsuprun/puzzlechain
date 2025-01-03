"""You are kindly requested to devise a solution for a coding task involving letter combinations. The task is to take a string composed of digits ranging from 2 to 9 and return all possible letter combinations that correspond to those numbers, much like the mapping found on telephone buttons. 

The mapping is as follows:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please remember to filter out any non-digit characters, including ones and zeros, from the input string.

Here are a few examples to illustrate the requirements:

1. For the input `digits = "23"`, the expected output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should simply be an empty list: `[]`.
3. For the input `digits = "2"`, please return `["a","b","c"]`.
4. If the input is `digits = "12*30"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

You are encouraged to adhere to the constraints that the length of `digits` should be between 0 and 4, and that each character within `digits` must be a digit in the range of '2' to '9'.

The function signature for your solution should be: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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