"""You MUST solve this urgent coding challenge IMMEDIATELY! Given a string containing digits from 2-9 inclusive, your task is to return ALL possible letter combinations that the number could represent. It's CRUCIAL that you return the answer in ANY order. 

Refer to the digit-letter mapping below, which is ESSENTIAL for your solution:

- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Remember, the input number may include non-digit characters, zeros, or ones, so you MUST filter them out IMMEDIATELY!

Here are some crucial examples to guide your solution:

1. Input: digits = "23" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: digits = "" should yield Output: []
3. Input: digits = "2" should yield Output: ["a","b","c"]
4. Input: digits = "12*30" should yield Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep in mind the following constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

The function signature for your urgent implementation is: letterCombinations(digits: str) -> list[str] 

Get to work and deliver a solution NOW! Time is of the essence!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
    filtered_digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations