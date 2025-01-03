"""Alright, genius, listen up! You've got a string of digits from 2 to 9, and your job is to figure out all the possible letter combos those numbers can represent. You know, like how we used to text back in the stone age with those old-school phone keypads. Here's the mapping if you somehow forgot:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and do me a favor: if there are any non-digit characters, ones, or zeros in there, just toss 'em out like yesterday's trash. 

Here's a few examples to get that brain of yours churning:

Example 1: 
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Example 4:
Input: digits = "12*30"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

And hey, just a reminder: keep the length of those digits between 0 and 4, and make sure they're from the range of ['2', '9']. 

Now go ahead and write that function: letterCombinations(digits: str) -> list[str]. Don't mess it up!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and ones/zeros
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