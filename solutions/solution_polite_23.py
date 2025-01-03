"""You are kindly requested to write a function that takes a string composed of digits ranging from 2 to 9. The goal is to return all possible letter combinations that these digits could represent, in any order that you find suitable. 

To assist you, here is the mapping of digits to their corresponding letters, similar to those found on telephone keypads:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may include non-digit characters, as well as ones or zeros. You are encouraged to filter these out before proceeding.

Here are a few examples to guide your implementation:

1. For the input `digits = "23"`, you would return: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
2. If the input is `digits = ""`, the expected output would be: `[]`
3. For the input `digits = "2"`, you should return: `["a","b","c"]`
4. In the case where `digits = "12*30"`, the output should again be: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

Please ensure that your function adheres to the following constraints:

- The length of the input string can range from 0 to 4.
- Each character in the string must be a digit between '2' and '9'.

The function signature is as follows: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to these details, and I wish you the best in crafting your solution!"""

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
    
    # Filter out non-digit characters and invalid digits
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