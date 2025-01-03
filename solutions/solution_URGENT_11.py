"""URGENT: Your task is to solve a critical coding problem NOW! You must write a function that takes a string of digits (ranging from 2 to 9) and returns ALL possible letter combinations that these digits can represent, based on the classic telephone keypad mapping. 

Be aware that the input may include non-digit characters, as well as zeroes and ones, which you must filter out IMMEDIATELY!

Here's the mapping you MUST utilize:
- Button 2: ABC
- Button 3: DEF
- Button 4: GHI
- Button 5: JKL
- Button 6: MNO
- Button 7: PQRS
- Button 8: TUV
- Button 9: WXYZ

Examples to guide your solution:
1. For input digits = "23", the expected output is ["ad","ae","af","bd","be","bf","cd","ce","cf"].
2. For input digits = "", the output should be [].
3. For input digits = "2", expect ["a","b","c"].
4. For input digits = "12*30", the output must include ["ad","ae","af","bd","be","bf","cd","ce","cf"].

Keep the constraints in mind:
- The length of digits can be from 0 to 4.
- Each digit must be in the range ['2', '9'].

The function signature you need to implement is: letterCombinations(digits: str) -> list[str].

Time is of the essence! Get started NOW!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only '2' to '9'
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