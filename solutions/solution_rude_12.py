"""You’ve got a string full of digits from 2 to 9, and your job is to spit out every possible letter combo these numbers can create. That’s right, just like those old-school phone keypads. Here’s the mapping if you need a reminder:

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

Oh, and don’t waste your time with any weird characters, zeros, or ones. Just scrub them out and get to work!

Here are some examples if you're struggling:

Input: "23" should give you: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Input: "" should return: []
Input: "2" should be: ["a","b","c"]
Input: "12*30" should also give: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Keep your output in any order you like, but remember—no more than 4 characters in that digits string. And the function signature? It’s letterCombinations(digits: str) -> list[str]. Now quit dawdling and get it done!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out invalid characters
    digits = ''.join(filter(lambda x: x in digit_to_char, digits))
    
    if not digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(digits):
            combinations.append(path)
            return
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations