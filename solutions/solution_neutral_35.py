"""Given a string consisting of digits between 2 and 9, your task is to return all possible letter combinations that the number could represent, in any order. 

The mapping of digits to letters is as follows:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

If the input contains any non-digit characters, such as 1 or 0, they should be removed.

Example inputs and expected outputs are:

1. Input: "23"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

2. Input: ""
   Output: []

3. Input: "2"
   Output: ["a", "b", "c"]

4. Input: "12*30"
   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

The length of the digits string can range from 0 to 4, with each character being a digit between '2' and '9'.

The function signature should be: `letterCombinations(digits: str) -> list[str]`"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid digits
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