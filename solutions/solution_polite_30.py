"""You are invited to tackle a delightful coding challenge. The task is to take a string that consists of digits from 2 to 9 and return all the possible letter combinations that these digits could represent, similar to the mappings found on a telephone keypad.

Here are the mappings for your reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input may contain some non-digit characters, as well as ones or zeros, which you should kindly filter out.

To illustrate, here are a few examples:

1. For an input of `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If the input is `digits = ""`, the output should simply be `[]`.
3. With an input of `digits = "2"`, you should yield `["a","b","c"]`.
4. Lastly, for an input of `digits = "12*30"`, you would again return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that the constraints are adhered to: the length of the digits string should be between 0 and 4, and each character in the string must be a digit in the range from '2' to '9'.

The function signature for your implementation will be: `letterCombinations(digits: str) -> list[str]`.

I wish you the very best in your coding endeavor!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and '1' or '0'
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