"""You are invited to solve an engaging coding challenge. The task involves taking a string composed of digits ranging from 2 to 9 and returning all possible letter combinations that these digits could represent, similar to how letters correspond to buttons on a telephone. 

Below is the mapping for reference:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Please note that the input string may contain non-digit characters, as well as ones or zeros, which should be filtered out. 

To illustrate, here are some examples:

1. If the input is `digits = "23"`, the expected output would be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input, `digits = ""`, the output should be `[]`.
3. When the input is `digits = "2"`, the output would be `["a","b","c"]`.
4. In the case of `digits = "12*30"`, you should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

For your function, please use the following signature: `letterCombinations(digits: str) -> list[str]`.

I hope you find this task both enjoyable and rewarding!"""

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