"""Please write a function that takes a string consisting of digits from 2 to 9 and returns all the possible letter combinations that the number could represent. For your reference, here is the mapping of digits to letters, similar to what you would find on a telephone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Kindly note that the input may include non-digit characters, as well as the digits one or zero. Please filter these out for your final result.

Here are a few examples to illustrate:

1. If the input is "23", the expected output would be ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. If the input is an empty string "", the output should be an empty list [].
3. For the input "2", the result should be ["a","b","c"].
4. If the input is "12*30", you should return ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Please ensure that the constraints are taken into account: the length of the digits should be between 0 and 4, and each digit should be in the range ['2', '9'].

The function signature should be: letterCombinations(digits: str) -> list[str]. Thank you for your attention to detail in this task!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    
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