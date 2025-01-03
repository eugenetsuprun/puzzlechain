"""You're in a race against time! You need to decode a string of digits from 2-9 into every possible combination of letters they can represent, just like the old phone keypads! 

Your task is to implement the function `letterCombinations(digits: str) -> list[str]`. This function must take a string containing only the digits 2-9, filter out any non-digit characters, and return all the possible letter combinations those digits can form. 

Be mindful of the fact that:
- Button 2 corresponds to "ABC"
- Button 3 corresponds to "DEF"
- Button 4 corresponds to "GHI"
- Button 5 corresponds to "JKL"
- Button 6 corresponds to "MNO"
- Button 7 corresponds to "PQRS"
- Button 8 corresponds to "TUV"
- Button 9 corresponds to "WXYZ"

Time is ticking! The output must be returned in any order, and here are some examples to guide you:

1. If `digits = "23"`, you should return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.
2. If `digits = ""`, the result is `[]`.
3. If `digits = "2"`, the output must be `["a","b","c"]`.
4. If `digits = "12*30"`, filter it down and return `["ad","ae","af","bd","be","bf","cd","ce","cf"]`.

Remember, the length of `digits` can be between 0 and 4, and you must only deal with valid digits in the range ['2', '9']. 

Get to it now and don't let the clock run out!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = phone_map[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    digits = ''.join(filter(str.isdigit, digits))
    combinations = []
    backtrack(0, "")
    return combinations