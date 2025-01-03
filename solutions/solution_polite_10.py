"""You are invited to solve an intriguing coding challenge involving letter combinations derived from a string of digits. The task is to return all possible letter combinations that the given digits could represent, adhering to the mapping of digits to letters found on telephone buttons. 

The mapping is as follows:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as the digits '1' or '0', which you should kindly filter out.

Here are some examples to guide you:
1. For the input `digits = "23"`, the expected output is `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should simply be `[]`.
3. When the input is `digits = "2"`, the output should be `["a","b","c"]`.
4. For the input `digits = "12*30"`, you would expect to receive `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

The constraints to keep in mind are that the length of the digits string will range from 0 to 4, and each character in the string must be a digit in the range from '2' to '9'.

Please implement your solution using the following function signature: `letterCombinations(digits: str) -> list[str]`. 

Best of luck with this delightful coding task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            backtrack(index + 1, path + char)
    
    combinations = []
    backtrack(0, "")
    return combinations