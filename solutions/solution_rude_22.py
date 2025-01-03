"""Alright genius, here’s the deal. You’ve got this string full of digits from 2 to 9, and your task is to spit out every possible combination of letters those numbers could stand for. It’s like your phone's keypad, you know? 

Here’s the breakdown of the digits:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and don’t waste my time with any non-digit garbage, like ones or zeros. Just kick those to the curb.

Let’s see some examples so you don’t mess this up:

1. Input: "23" should give you: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" should return: []
3. Input: "2" should spit out: ["a","b","c"]
4. Input: "12*30" should come back with: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep it simple, alright? Your precious function should look like this: `letterCombinations(digits: str) -> list[str]` 

Now go on, impress me."""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters
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