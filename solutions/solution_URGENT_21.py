"""Your mission is CRUCIAL! You must take a string of digits ranging from 2 to 9 and decipher ALL possible letter combinations that these numbers can represent. We have a mapping of digits to letters, similar to what you find on a phone keypad:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

IMPORTANT: The input may contain non-digit characters, as well as ones and zeros. You MUST filter these out! 

Consider the following examples as critical test cases:

1. **Input:** digits = "23"
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

2. **Input:** digits = ""
   **Output:** []

3. **Input:** digits = "2"
   **Output:** ["a","b","c"]

4. **Input:** digits = "12*30"
   **Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"]

You are limited by the constraint: 0 <= digits.length <= 4, and each digits[i] must be between '2' and '9'.

Your function signature MUST be: letterCombinations(digits: str) -> list[str]

Time is of the essence—GET TO WORK!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
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