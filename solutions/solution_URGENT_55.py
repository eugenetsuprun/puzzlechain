"""You need to act fast! Your task is to write a function that takes a string of digits between 2 and 9 and returns all possible letter combinations those digits could represent, just like the old telephone keypads. 

Here's the mapping you must use:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Be careful! You must ignore any non-digit characters, zeros, or ones. 

Check these examples closely:

1. Input: "23" -> Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
2. Input: "" -> Output: []
3. Input: "2" -> Output: ["a","b","c"]
4. Input: "12*30" -> Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Stay focused on the constraints: 
- The length of the input string can be between 0 and 4.
- Ensure digits are in the range ['2', '9'].

Your function should look like this: `letterCombinations(digits: str) -> list[str]`. Time is of the essence—get it done NOW!"""

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