"""Please write a function that takes a string containing digits from 2 to 9 and returns all possible letter combinations that the number could represent, as per the traditional telephone button mapping provided below:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

If the input string contains any non-digit characters, such as ones or zeros, kindly filter them out. 

Here are a few examples to illustrate the expected functionality:

1. If the input is `digits = "23"`, the output should be `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. For an empty input, `digits = ""`, the output should be `[]`.
3. With a single digit, `digits = "2"`, the expected output is `["a","b","c"]`.
4. Lastly, if the input is `digits = "12*30"`, the function should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Please ensure that the function signature is as follows: `letterCombinations(digits: str) -> list[str]`. Thank you for your attention to detail!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    digits = ''.join(filter(lambda x: x in phone_map, digits))
    
    if not digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations